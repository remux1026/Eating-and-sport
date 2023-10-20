package NutrifitDatabase;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;

public class CreateNewUserMySQL implements ICreateNewUser{

	
	@Override
	public void createUser(String username, String email, String password, String sex, String birthday,
			String firstname, String lastname, double weight, double height) {
		Connection conn = null;
		Statement statement = null;
		
		try {
			conn = JDBCUtilities.getDataSource().getConnection();
			String query = String.format("insert into UserLogging.`USER PROFILE` (Email, Username, Password, FirstName, LastName, Sex, Birthday, Height, Weight) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', %.2f, %.2f)", 
					email, username, password, firstname, lastname, sex, birthday, height, weight);
			statement = conn.createStatement();
			statement.execute(query);
			
			JDBCUtilities.close(conn, statement, null);
		}catch(SQLException e) {
			JDBCUtilities.close(conn, statement, null);
		}
	}
}