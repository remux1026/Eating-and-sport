package NutrifitDatabase;
import java.util.Map;

public class CalculateCaloriesBurntDemo {
	public static void main(String[] args) {
		IManageUserData user = new ManageUserDataMySQL();
		
		user.setUser("123", "123");
		double weight = Double.valueOf(user.getProfileData().get("Weight"));
		Map<String, String> randomExerciseRecord = user.getUserExercises().get(0);
		
		double caloriesBurnt = CalculationsUtilities.calculateCaloriesBurnt(
				randomExerciseRecord.get("Intensity"),
				Double.valueOf(randomExerciseRecord.get("Duration")), 
				weight);
		
		System.out.println("Calories Burnt (kJ): " + caloriesBurnt);
		
		user.close();
	}
}
