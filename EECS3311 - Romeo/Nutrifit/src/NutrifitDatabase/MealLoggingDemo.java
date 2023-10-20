package NutrifitDatabase;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class MealLoggingDemo {
	public static void main(String[] args) {
		IManageUserData user = new ManageUserDataMySQL();
		
		user.setUser("2309812093821", "password");
		
		List<Map<String, String>> ingredients = new ArrayList<>();
		
		Map<String, String> ingredient1 = new HashMap<>();
		ingredient1.put("FoodID", "2");
		ingredient1.put("Amount", "23.6");
		
		ingredients.add(ingredient1);
		
		user.insertUserMeal("Dinner with family", "2023-10-05", "D", ingredients);
		
		System.out.println(user.getUserMeals());

		user.close();
		
	}
}
