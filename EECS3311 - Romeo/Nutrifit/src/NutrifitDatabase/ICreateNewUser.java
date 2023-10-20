package NutrifitDatabase;

/**
 * will be refactored later
 * @author Joshua Chen
 *
 */
public interface ICreateNewUser {
	/**
	 * Records a new user into the database
	 * @param username
	 * @param email
	 * @param password
	 * @param sex gender can be in the domain {'M', 'F'}
	 * @param birthday birthday must be in the date format 'yyyy-mm-dd'
	 * @param firstname
	 * @param lastname
	 * @param weight the weight in kg
	 * @param height in cm
	 * @throws Exception
	 * @returns returns false if the users account was not recorded
	 */
	public void createUser(String username, String email, String password, String sex, String birthday,
			String firstname, String lastname, double weight, double height);
		
}



