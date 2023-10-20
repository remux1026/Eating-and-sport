package NutrifitDatabase;
public class CalculateBMRDemo {
	public static void main(String[] args) {
		IManageUserData user = new ManageUserDataMySQL();
		
		user.setUser("123", "123");
		
		java.util.Map<String, String> profile = user.getProfileData();
		
		double BMR = CalculationsUtilities.bmr(profile.get("Birthday"), profile.get("Sex"), 
				Double.valueOf(profile.get("Height")), Double.valueOf(profile.get("Weight")));
		
		System.out.println(BMR);
		user.close();
	}
}
