package NutrifitDatabase;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class CalculateNutrientsDemo {
	public static void main(String[] args) {
		IManageUserData user = new ManageUserDataMySQL();
		
		user.setUser("123", "123");
		List<Map<String, String>> meals = user.getUserMeals().stream().
					filter(tuple -> tuple.get("MealName").contains("Snack")).collect(Collectors.toList());
		
		String randomMealID = meals.get(0).get("MealID");
		
		
		List<Map<String, String>> mealIngredients = user.getUserMealIngredients().stream().
				filter(tuple -> tuple.get("MealID").equals(randomMealID)).collect(Collectors.toList());
		
		System.out.println("meal calories: " + CalculationsUtilities.getMealCalories(mealIngredients));
		System.out.println("meal nutrient breakdown: " + CalculationsUtilities.nutritionBreakdown(mealIngredients));
		
		user.close();
	}
}
