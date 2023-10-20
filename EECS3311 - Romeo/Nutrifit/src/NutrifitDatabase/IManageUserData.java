package NutrifitDatabase;
import java.util.List;
import java.util.Map;


/**
 * This interfaces manages data for a specific user in the UserLogging database utilizes a pessimistic locking mechanism 
 * to handle concurrent user accesses.
 * @author Joshua Chen
 *
 */
public interface IManageUserData {
	public List<Map<String, String>> getUserMeals();
	
	public List<Map<String, String>> getUserMealIngredients();
	
	public List<Map<String, String>> getUserExercises();
	
	public Map<String, String> getProfileData();
	
	/**
	 * 
	 * @param email
	 * @return returns false if the email was not set in the user profile
	 */
	public boolean setEmail(String email);
	/**
	 * 
	 * @param height 
	 * @return returns false if the height was not set in the user profile
	 */
	public boolean setHeight(double height);
	
	/**
	 * 
	 * @param height 
	 * @return returns false if the weight was not set in the user profile
	 */
	public boolean setWeight(double weight);
	
	/**
	 * @param sex the gender is in the domain {'M', 'F'}
	 * @return returns false if the sex was not set in the user profile
	 */
	public boolean setSex(String sex);
	
	/**
	 * 
	 * @param firstName
	 * @param lastName
	 * @return returns false if the first name or last name was not set in the user profile
	 */
	public boolean setName(String firstName, String lastName);
	
	/**
	 * 
	 * @param birthday the birthday is always in the form 'yyyy-mm-dd'
	 * @return returns false if the birthday was not set in the user profile
	 */
	public boolean setBirthday(String birthday);
	
	/**
	 * returns an update code represented as an integer. 
	 * code '0' = input success
	 * code '1' = no insert operation was done
	 * code '2' = partial insert or no insert operation was done
	 * @param name
	 * @param date date must be in the form 'yyyy-mm-dd'
	 * @param type type can be in the domain {'B', 'D', 'S'} where the character B represents breakfast, D represents dinner, and S represents snack
	 * @param ingrediants 
	 * are of the form Map<String, String> where each element in the list is a tuple with the following mapping pairs 
	 * "FoodID" -> integer of the ID, "Amount" -> the amount in decimal form as string in grams.
	 * @return
	 * @throws Exception
	 */
	public int insertUserMeal(String name, String date, String type, List<Map<String, String>> ingredients);
	
	/**
	 * returns false if no insert occurred.
	 * @param intensity intensity can be in the domain of {'V', 'H', 'M', 'L'} 
	 * @param type the name of this exercise
	 * @param duration
	 * @param date date must be in the form 'yyyy-mm-dd hh:mm:ss'
	 * @return
	 * @throws Exception
	 */
	public boolean insertUserExercise(String intensity, String type, double duration, String date);
	
	
	/**
	 * returns false if no deletion of the specified mealID record occurred.
	 * @Warning deleting a meal record will cascade to the ingredients table.
	 * @param mealID
	 * @return
	 * @throws Exception
	 */
	public boolean deleteUserMeal(int mealID);
	
	
	/**
	 * returns false if no deletion of the specified exerciseID record occurred.
	 * @param exerciseID
	 * @return
	 * @throws Exception
	 */
	public boolean deleteUserExercise(int exerciseID);
	
	/**
	 * sets a specific user for this instance.
	 * when a user is set the table fragment of this user will be locked and unable for use until the 
	 * close() method is called.
	 * returns an update code represented as an integer. 
	 * code '0' = user correctly identified
	 * code '1' = user credentials are not correct
	 * code '2' = another instance of this user is in use
	 * code '3' = server unresponsive
	 * @param username
	 * @param password
	 * @return
	 * @throws Exception
	 */
	public int setUser(String username, String password);
	
	/**
	 * resets user instance and frees the table fragment from the locked state
	 */
	public void close();
}
