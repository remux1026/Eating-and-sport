package NutrifitDatabase;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.List;
import java.util.Map;
import java.sql.Connection;
import java.util.Collections;
import java.util.HashMap;

/**
* Implements the IManageUserData interface. Utilizes a WRITE-THROUGH technique for caching
* Application <=> cache <=> USER LOGGING Database.
* @author Joshua Chen
*/
public class ManageUserDataMySQL implements IManageUserData{
	
	//a fragment of the UserLogging DB into memory
	private List<Map<String, String>> userMeals;
	private List<Map<String, String>> userExercises;
	private List<Map<String, String>> userMealIngredients;
	private Map<String, String> userProfile;
	private int userID;
	
	private boolean verified() {
		return this.userMeals != null && this.userExercises != null && this.userMealIngredients != null;
	}
	
	@Override
	public int setUser(String username, String password){
		close();
		
		Connection connection = null;
		Statement statement = null;
		ResultSet set = null;
		try {
			connection = JDBCUtilities.getDataSource().getConnection();
			statement = connection.createStatement();
			String query = String.format("SELECT * FROM `UserLogging`.`USER PROFILE` where `Username` = \"%s\"",username);		
			set = statement.executeQuery(query);
			
			if(!set.next() || !set.getString("Password").equals(password)) {
				return 1;
			}
			
			if(set.getBoolean("Locked")) {
				return 2;
			}
			
			//populate memory
			this.userID = set.getInt("UserID");
			this.userProfile = JDBCUtilities.extractResult(set = statement.executeQuery(query)).get(0);
			
			query = String.format("SELECT * FROM UserLogging.`USER MEAL` where `UserMealID` = %d;" ,this.userID);
			set = statement.executeQuery(query);
			this.userMeals = JDBCUtilities.extractResult(set);
				
			query = String.format("SELECT * FROM `UserLogging`.`USER EXERCISE` where `UserExerciseID` = %d" , this.userID);
			set = statement.executeQuery(query);
			this.userExercises = JDBCUtilities.extractResult(set);
				
			query = String.format("SELECT * FROM `UserLogging`.`USER MEAL INGREDIANTS` where `UserIngrediantID` = %d" , this.userID);
			set = statement.executeQuery(query);
			this.userMealIngredients = JDBCUtilities.extractResult(set);
			
			//THIS INSTANCE IS COMPLETELY LOCKED NO INSTANCE CAN MODIFY THIS FRAGMENT OF THE USER LOGGING DB
			query = String.format("update UserLogging.`USER PROFILE` set Locked = True where userID = %d", this.userID);
			statement.executeUpdate(query);

			JDBCUtilities.close(connection, statement, set);
			return 0;
		}catch(SQLException e) {
			JDBCUtilities.close(connection, statement, set);
			close();
			return 3;
		}
	}
	
	private boolean updateUserFields(String field, String value) {
		if(!verified()) {
			return false;
		}
		
		Connection conn = null;
		Statement statement = null;
		
		try {
			//update db
			conn = JDBCUtilities.getDataSource().getConnection();
			statement = conn.createStatement();
			String query = String.format("update UserLogging.`USER PROFILE` set %s = '%s' where userID = %d", field, value, this.userID);
			statement.executeUpdate(query);
			JDBCUtilities.close(conn, statement, null);
			
			//now update cache
			this.userProfile.put(field, value);
			return true;
		}catch(SQLException e) {
			JDBCUtilities.close(conn, statement, null);
			return false;
		}
	}
	
	@Override
	public boolean setEmail(String email) {
		return updateUserFields("Email", email);
	}
	
	@Override
	public boolean setHeight(double height) {
		return updateUserFields("Height", String.valueOf(height));
	}

	@Override
	public boolean setWeight(double weight) {
		return updateUserFields("Weight", String.valueOf(weight));
	}
	
	@Override
	public boolean setSex(String sex) {
		return updateUserFields("Sex", sex);
	}

	@Override
	public boolean setName(String firstName, String lastName) {
		return updateUserFields("firstName", firstName) & updateUserFields("lastName", lastName);
	}

	@Override
	public boolean setBirthday(String birthday) {
		return updateUserFields("Birthday", birthday);
	}
	
	@Override
	public Map<String, String> getProfileData(){
		return verified() ? Collections.unmodifiableMap(this.userProfile) : null;
	}
	
	@Override
	public List<Map<String, String>> getUserMeals() {
		return verified() ? Collections.unmodifiableList(this.userMeals) : null;
	}
	
	@Override
	public List<Map<String, String>> getUserMealIngredients(){
		return verified() ? Collections.unmodifiableList(this.userMealIngredients) : null;
	}

	@Override
	public List<Map<String, String>> getUserExercises(){
		return verified() ? Collections.unmodifiableList(this.userExercises) : null;
	}

	@Override
	public int insertUserMeal(String name, String date, String type, List<Map<String, String>> ingredients){
		if(!verified()) {
			return 1;
		}
		
		Connection conn = null;
		Statement statement = null;
		ResultSet rs = null;
		
		try {
			//write to db first
			conn = JDBCUtilities.getDataSource().getConnection();
			statement = conn.createStatement();
			String query = String.format("insert into UserLogging.`USER MEAL` (UserMealID, MealName, Date, Type) values (%d, '%s', '%s', '%s')",
					this.userID, name, date, type);
			statement.executeUpdate(query, Statement.RETURN_GENERATED_KEYS);
			rs = statement.getGeneratedKeys();
			rs.next();
			int mealKey = rs.getInt(1);
			
			//update cache
			Map<String, String> mealRecord = new HashMap<>();
			mealRecord.put("MealID", String.valueOf(mealKey));
			mealRecord.put("UserMealID", String.valueOf(this.userID));
			mealRecord.put("MealName", name);
			mealRecord.put("Date", date);
			mealRecord.put("Type", type);
			this.userMeals.add(mealRecord);
			
			for(Map<String, String> ingrediant: ingredients) {
				//write to db first
				query = String.format("insert into UserLogging.`USER MEAL INGREDIANTS` (MealID, UserIngrediantID, FoodID, Amount) values (%d, %d, %s, %s)",
						mealKey, this.userID, ingrediant.get("FoodID"), ingrediant.get("Amount"));
				statement.executeUpdate(query, Statement.RETURN_GENERATED_KEYS);
				rs = statement.getGeneratedKeys();
				rs.next();
				int ingrediantKey = rs.getInt(1);
				
				//update cache
				Map<String, String> ingrediantRecord = new HashMap<>();
				ingrediantRecord.put("IngrediantID", String.valueOf(ingrediantKey));
				ingrediantRecord.put("MealID", String.valueOf(mealKey));
				ingrediantRecord.put("UserIngrediantID", String.valueOf(this.userID));
				ingrediantRecord.put("FoodID", String.valueOf(ingrediant.get("FoodID")));
				ingrediantRecord.put("Amount", String.valueOf(ingrediant.get("Amount")));
				this.userMealIngredients.add(ingrediantRecord);
			}
			
			JDBCUtilities.close(conn, statement, rs);
			return 0;
		}catch(SQLException e) {
			JDBCUtilities.close(conn, statement, rs);
			return 2;
		}
	}

	@Override
	public boolean insertUserExercise(String intensity, String type, double duration, String date){
		if(!verified()) {
			return false;
		}
		
		Connection conn = null;
		Statement statement = null;
		ResultSet rs = null;
		
		try {
			//populate db first
			conn = JDBCUtilities.getDataSource().getConnection();
			statement = conn.createStatement();
			String query = String.format("insert into UserLogging.`USER EXERCISE` (UserExerciseID, Intensity, Type, Duration, DateTime) values (%d, '%s', '%s', %.2f, '%s')",
					this.userID, intensity, type, duration, date);
			statement.executeUpdate(query, Statement.RETURN_GENERATED_KEYS);
			rs = statement.getGeneratedKeys();
			rs.next();
			int exerciseID = rs.getInt(1);
			JDBCUtilities.close(conn, statement, rs);
			
			//update cache
			Map<String, String> exerciseRecord = new HashMap<>();
			exerciseRecord.put("ExerciseID", String.valueOf(exerciseID));
			exerciseRecord.put("UserExerciseID", String.valueOf(this.userID));
			exerciseRecord.put("Intensity", intensity);
			exerciseRecord.put("Duration", String.valueOf(duration));
			exerciseRecord.put("DateTime", date);
			exerciseRecord.put("Type", type);
			this.userExercises.add(exerciseRecord);
			
			return true;
		}catch(SQLException e){
			JDBCUtilities.close(conn, statement, rs);
			return false;
		}
	}
	
	@Override
	public boolean deleteUserMeal(int mealID){
		if(!verified()) {
			return false;
		}
		
		Connection conn = null;
		Statement statement = null;
		int orgSize = this.userMeals.size();
		try {
			//update db first
			conn = JDBCUtilities.getDataSource().getConnection();
			statement = conn.createStatement();
			String query = String.format("delete from UserLogging.`USER MEAL` where mealID = %d", mealID);
			statement.executeUpdate(query);
			JDBCUtilities.close(conn, statement, null);
			
			//now update cache
			this.userMeals.removeIf(tuple -> tuple.get("MealID").equals(String.valueOf(mealID)));
			this.userMealIngredients.removeIf(tuple -> tuple.get("MealID").equals(String.valueOf(mealID)));
			
			return orgSize < this.userMeals.size();
		}catch(SQLException e) {
			JDBCUtilities.close(conn, statement, null);
			return false;
		}
	}

	@Override
	public boolean deleteUserExercise(int exerciseID){
		if(!verified()) {
			return false;
		}
		
		Connection conn = null;
		Statement statement = null;
		int orgSize = this.userExercises.size();
		try {
			//update db first
			conn = JDBCUtilities.getDataSource().getConnection();
			statement = conn.createStatement();
			String query = String.format("delete from UserLogging.`USER EXERCISE` where ExerciseID = %d", exerciseID);
			statement.executeUpdate(query);
			JDBCUtilities.close(conn, statement, null);
			
			//now update cache
			this.userExercises.removeIf(tuple -> tuple.get("ExerciseID").equals(String.valueOf(exerciseID)));
			
			return orgSize < this.userExercises.size();
		}catch(SQLException e) {
			JDBCUtilities.close(conn, statement, null);
			return false;
		}
	}

	/**
	 * unlocks this database fragment
	 */
	@Override
	public void close() {
		this.userExercises = null;
		this.userMealIngredients = null;
		this.userMeals = null;
		
		Connection conn = null;
		Statement statement = null;
		try {
			conn = JDBCUtilities.getDataSource().getConnection();
			statement = conn.createStatement();
			
			//unlock this database fragment
			String query = String.format("update UserLogging.`USER PROFILE` set Locked = False where userID = %d", this.userID);
			statement.executeUpdate(query);
			JDBCUtilities.close(conn, statement, null);
		}catch(SQLException e) {
			JDBCUtilities.close(conn, statement, null);
		}
		this.userID = 0;
	}
}