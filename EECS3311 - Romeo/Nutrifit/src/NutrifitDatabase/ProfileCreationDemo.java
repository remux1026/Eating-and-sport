package NutrifitDatabase;

public class ProfileCreationDemo {
	
	public static void main(String[] args) {
		ICreateNewUser newUser = new CreateNewUserMySQL();
		
		newUser.createUser("2309812093821", "129038132083@gmail.com", "password", "M", "1999-10-20", "Joe", "John",91, 181);
		
		
		IManageUserData user = new ManageUserDataMySQL();
		user.setUser("2309812093821", "password");
		
		System.out.println(user.getProfileData());
		
		user.close();
	}
}
