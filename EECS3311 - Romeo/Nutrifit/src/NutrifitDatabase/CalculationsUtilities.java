package NutrifitDatabase;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.time.Duration;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;

public class CalculationsUtilities {
	
	private CalculationsUtilities(){}
	
	private static double nutrientCalculation(List<Map<String, String>> IngredientList,String nutrientCode){
        IGetNutrientData data=new NutrientData(new NutrientDataMySQL());
        double nutrientAmount=0;
        for(Map<String, String> ingredient:IngredientList) {
            List<Map<String,String>> temp=data.getFoodData(Integer.valueOf(ingredient.get("FoodID")));

            Optional<Map<String, String>> nutrients = temp.stream().
            		filter(v->v.get("NutrientID").equals(nutrientCode)).findFirst();
            double nutrientValue = 0;
            nutrientValue = nutrients.isPresent() ? Double.valueOf(nutrients.get().get("NutrientValue")) : 0;
            double factor=nutrientValue/100;
            nutrientAmount+=Double.valueOf(ingredient.get("Amount"))*factor;
        }

        return nutrientAmount;
    }

    public static Map<String, Double> nutritionBreakdown(List<Map<String, String>> IngredientList){
        double protein=nutrientCalculation(IngredientList,"203");
        double calories=nutrientCalculation(IngredientList,"268");
        double carb=nutrientCalculation(IngredientList,"205");
        double vitaminB6=nutrientCalculation(IngredientList,"415");
        double vitaminB12=nutrientCalculation(IngredientList,"418");
        double vitaminC=nutrientCalculation(IngredientList,"401");

        double totalWeight=IngredientList.stream().mapToDouble(tuple->Double.valueOf(tuple.get("Amount"))).sum();
        double other=totalWeight-protein-carb-vitaminB6-vitaminB12-vitaminC;
        Map<String, Double> resultMap= new HashMap<>();
        resultMap.put("Protein",protein);
        resultMap.put("Calories",calories);
        resultMap.put("Carbs",carb);
        resultMap.put("VitaminB6",vitaminB6);
        resultMap.put("VitaminB12",vitaminB12);
        resultMap.put("VitaminC",vitaminC);
        resultMap.put("Other",other);

        return resultMap;
    }
    
    public static double getMealCalories(List<Map<String, String>> IngredientList) {
    	return nutrientCalculation(IngredientList, "268");
    }
    
    public static double calculateCaloriesBurnt(String intensity, double duration, double weight) {
    	Map<String, Double> MET = new HashMap<>();
    	MET.put("L", 3.0);
    	MET.put("M", 4.0);
    	MET.put("H", 5.0);
    	MET.put("V", 6.0);

        return (duration*60.0*(MET.get(intensity) * 3.5 * weight)) / 200.0;
    }
    
    /**
     * 
     * @param birthday birthday format in yyyy-mm-dd
     * @param height
     * @param weight
     * @param gender in th domain {'M', 'F'}
     * @return
     */
    public static double bmr(String birthday, String sex, double height, double weight) {
    	LocalDate d1 = LocalDate.parse(birthday, DateTimeFormatter.ISO_LOCAL_DATE);
    	LocalDate d2 = LocalDate.parse(birthday, DateTimeFormatter.ISO_LOCAL_DATE);
    	Duration diff = Duration.between(d1.atStartOfDay(), d2.atStartOfDay());
    	long age = diff.toDays();
    	
    	double bmrM = ((10 * weight) + (6.25 * height) - (5 * age) + 5);
    	double bmrF = ((10 * weight) + (6.25 * height) - (5 * age) - 161);
        return sex.equals("M") ? bmrM : bmrF;
    }
}
