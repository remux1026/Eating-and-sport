package NutrifitDatabase;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;

public class NutrientDataMySQL implements IGetNutrientData{

	@Override
	public List<Map<String, String>> getFoodData(int FoodID){
		Connection conn = null;
		Statement statement = null;
		ResultSet set = null;
		List<Map<String, String>> results = new ArrayList<>();
		
		try {
			conn = JDBCUtilities.getDataSource().getConnection();
			statement = conn.createStatement();
			String query = String.format("SELECT * FROM CanadianNutrientDB.`NutrientValuesTB` where FoodID = %d", FoodID);
			set = statement.executeQuery(query);
			
			results = JDBCUtilities.extractResult(set);
			JDBCUtilities.close(conn, statement, set);
			
			return results;
		}catch(SQLException e) {
			JDBCUtilities.close(conn, statement, set);
			return null;
		}
	}
}
