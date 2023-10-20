package NutrifitDatabase;

public class ExerciseLoggingDemo {
	public static void main(String[] args) {
		IManageUserData user = new ManageUserDataMySQL();
		
		user.setUser("2309812093821", "password");
		
		user.insertUserExercise("V", "Running", 1.5, "2023-10-19 00:00:00");
		
		System.out.println(user.getUserExercises());
		
		user.close();
	}
}
