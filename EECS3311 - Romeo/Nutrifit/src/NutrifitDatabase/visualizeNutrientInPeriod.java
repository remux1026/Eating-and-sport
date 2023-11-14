//visualizeNutrientInPeriod
package NutrifitDatabase;

import java.awt.Color;
import java.awt.GridLayout;
import java.security.KeyStore.Entry;
import java.text.DecimalFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.labels.StandardPieSectionLabelGenerator;
import org.jfree.chart.plot.MultiplePiePlot;
import org.jfree.chart.plot.PiePlot;
import org.jfree.chart.util.TableOrder;
import org.jfree.data.category.DefaultCategoryDataset;
import org.jfree.data.general.DefaultPieDataset;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.BoxLayout;




public class visualizeNutrientInPeriod {
	
	
	
	public static Map<String, Double> visualizeNutrientInPeriod(IManageUserData user,String startDate,String endDate)throws Exception {
		int days=(int) daysBetween(startDate, endDate);
		
		List<Map<String, String>> meals = user.getUserMeals();
		//System.out.println("meals:"+meals);
		List<String> mealIDs = getMealIDs(meals,startDate,endDate);
		//System.out.println("mealIDs:"+mealIDs);
		List<Map<String, String>> Ingredients = user.getUserMealIngredients();
		//System.out.println("Ingredients:"+Ingredients);
		List<Map<String, String>> takeIn=filterIngredientsByMealIDs(Ingredients,mealIDs);
		//System.out.println("takeIn:"+takeIn);
		//Map<String, Double> totalPeriodNutrient=CalculationsUtilities.nutritionBreakdown(takeIn);
		
		IGetNutrientData data=new NutrientData(new NutrientDataMySQL());
		Map<String, Double> totalPeriodNutrient=calculateTotalNutrients(takeIn, data);
		
		//we assume enegry is not a type of nutrient since it's unit is not in g,mg,or ug
		totalPeriodNutrient.remove("ENERGY (KILOJOULES)");
		totalPeriodNutrient.remove("ENERGY (KILOCALORIES)");
		
		unitconvert(totalPeriodNutrient);
		totalPeriodNutrient=sortNutrient(totalPeriodNutrient);
		System.out.println("totalPeriodNutrient:"+totalPeriodNutrient);

		//System.out.println("data of 630:"+data.getFoodData(630));
	
		
		
		Map<String, Double> avgPeriodNutrient=calculateAverageNutrients(totalPeriodNutrient,days);
		avgPeriodNutrient=sortNutrient(avgPeriodNutrient);
//		System.out.println("avgPeriodNutrient:"+avgPeriodNutrient);
//		avgPeriodNutrient.remove("ENERGY");
//		
		
		Map<String, Double> top5=getTopNAndOthers(avgPeriodNutrient, 5);
		Map<String, Double> top10=getTopNAndOthers(avgPeriodNutrient, 10);
		//unitConvert(avgPeriodNutrient);
		//unitConvert2(avgPeriodNutrient);
		
		//visualize
	    PieCompare pieCompare = new PieCompare();
	    pieCompare.visualize(top5, top10);
		
//		new PieChart().visualize(top5);
//		new PieChart().visualize(top10);
		return avgPeriodNutrient;
	}
	
	

	//get top N nutrients in the map
	public static Map<String, Double> getTopNAndOthers(Map<String, Double> avgPeriodNutrient, int n) {
	    Map<String, Double> topN = new LinkedHashMap<>();
	    String[] keys = avgPeriodNutrient.keySet().toArray(new String[0]);
	    Double[] values = avgPeriodNutrient.values().toArray(new Double[0]);
	    double others = 0;
	    for (int i = 0; i < keys.length; i++) {
	        if (i < n) {
	            topN.put(keys[i], values[i]);
	        } else {
	            others += values[i];
	        }
	    }
	    topN.put("other", others);
	    return topN;
	}

	
	//sort the map and make it from large to small
	public static Map<String, Double> sortNutrient(Map<String, Double> result) {
	    String[] keys = result.keySet().toArray(new String[0]);
	    Double[] values = result.values().toArray(new Double[0]);
	    for (int i = 0; i < values.length - 1; i++) {
	        for (int j = 0; j < values.length - 1 - i; j++) {
	            if (values[j] < values[j + 1]) {
	                double tempValue = values[j];
	                values[j] = values[j + 1];
	                values[j + 1] = tempValue;
	                String tempKey = keys[j];
	                keys[j] = keys[j + 1];
	                keys[j + 1] = tempKey;
	            }
	        }
	    }
	    Map<String, Double> sortedResult = new LinkedHashMap<>();
	    for (int i = 0; i < keys.length; i++) {
	        sortedResult.put(keys[i], values[i]);
	    }
	    return sortedResult;
	}

	
	//calculate all nutrients total amounts
	public static Map<String, Double> calculateTotalNutrients(List<Map<String, String>> takeIn, IGetNutrientData data) {
	    Map<String, Double> result = new HashMap<>();
	    for (Map<String, String> food : takeIn) {
	        double amount = Double.parseDouble(food.get("Amount"));
	        int foodID = Integer.parseInt(food.get("FoodID"));
	        List<Map<String, String>> nutrients = data.getFoodData(foodID);
	        for (Map<String, String> nutrient : nutrients) {
	            double nutrientValuePerGram = Double.parseDouble(nutrient.get("NutrientValue"));
	            String nutrientName = nutrient.get("NutrientName");
	            double totalNutrientValue = amount * nutrientValuePerGram;
	            result.put(nutrientName, result.getOrDefault(nutrientName, 0.0) + totalNutrientValue);
	        }
	    }
	    return result;
	}

	
	//input a map that contains the total amounts of different nutrients the use take in
	//return a map that divide those amount by number of days to get daily nutrient take in
	public static Map<String, Double> calculateAverageNutrients(Map<String, Double> totalPeriodNutrient, int days) {
        Map<String, Double> avgPeriodNutrient = new HashMap<>();
        for (Map.Entry<String, Double> entry : totalPeriodNutrient.entrySet()) {
            avgPeriodNutrient.put(entry.getKey(), entry.getValue() / days);
        }
        return avgPeriodNutrient;
    }
	
	//return a list of ingredients that been eaten in certain meals
	public static List<Map<String, String>> filterIngredientsByMealIDs(List<Map<String, String>> ingredients, List<String> mealIDs) {
        List<Map<String, String>> filteredIngredients = new ArrayList<>();
        for (Map<String, String> ingredient : ingredients) {
            if (mealIDs.contains(ingredient.get("MealID"))) {
                filteredIngredients.add(ingredient);
            }
        }
        return filteredIngredients;
    }
	
	
//	public void PieChartExample(Map<String, Double> avgPeriodNutrient) {
//        
//        DefaultPieDataset dataset = new DefaultPieDataset();
//        for (Map.Entry<String, Double> entry : avgPeriodNutrient.entrySet()) {
//            dataset.setValue(entry.getKey(), entry.getValue());
//        }
//
//        JFreeChart chart = ChartFactory.createPieChart(
//                "Nutrient Distribution",   // chart title
//                dataset,          // data
//                true,             // include legend
//                true,
//                false);
//
//        ChartPanel panel = new ChartPanel(chart);
//        setContentPane(panel);
//    }
	
	//get the mealIDs of all the meals the user eat during this period
	public static List<String> getMealIDs(List<Map<String, String>> meals, String startDate, String endDate) {
        List<String> mealIDs = new ArrayList<>();
        for (Map<String, String> meal : meals) {
            String date = meal.get("Date");
            if (date.compareTo(startDate) >= 0 && date.compareTo(endDate) <= 0) {
                mealIDs.add(meal.get("MealID"));
            }
        }
        return mealIDs;
    }
	
	
//	public static void unitConvert(Map<String, Double> avgPeriodNutrient) {
//		avgPeriodNutrient.put("VitaminB12", avgPeriodNutrient.get("VitaminB12")+1.1415*1.16);
//		avgPeriodNutrient.put("VitaminC", avgPeriodNutrient.get("VitaminC")+2.816*1.15);
//		avgPeriodNutrient.put("VitaminB6", avgPeriodNutrient.get("VitaminB6")+1.628*1.16);
//		
////		avgPeriodNutrient.put("DietaryFiber", 0.2816*2.28);
////		avgPeriodNutrient.put("FAT", 0.1628*1.616);
////		avgPeriodNutrient.put("ASH", 0.1628+1.616);
////		avgPeriodNutrient.put("CALCIUM", 1.616-0.2816);
////		avgPeriodNutrient.put("	FRUCTOSE", 1.1528-0.2816);
//		//avgPeriodNutrient.remove("VitaminB12");
//		avgPeriodNutrient.remove("Calories");
//    }
//	
//	public static void unitConvert2(Map<String, Double> avgPeriodNutrient) {
//		avgPeriodNutrient.put("VitaminB12", avgPeriodNutrient.get("VitaminB12")+1.1415*1.16);
//		avgPeriodNutrient.put("VitaminC", avgPeriodNutrient.get("VitaminC")+2.816*1.15);
//		avgPeriodNutrient.put("VitaminB6", avgPeriodNutrient.get("VitaminB6")+1.628*1.16);
//		
//		avgPeriodNutrient.put("DietaryFiber", 0.2816*2.28);
//		avgPeriodNutrient.put("FAT", 0.1628*16.16);
//		avgPeriodNutrient.put("ASH", 0.1628+1.616);
//		avgPeriodNutrient.put("CALCIUM", 1.616-0.2816);
//		avgPeriodNutrient.put("	FRUCTOSE", 1.1528-0.2816);
//		//avgPeriodNutrient.remove("VitaminB12");
//		avgPeriodNutrient.remove("Calories");
//    }
	
	//mg and ug to g
		public static void unitconvert(Map<String, Double> totalPeriodNutrient) {
			String[] compound= {"DIETARY FOLATE EQUIVALENTS","LUTEIN AND ZEAXANTHIN","OXALIC ACID","CAFFEINE","THEOBROMINE","CALCIUM","IRON","MAGNESIUM","PHOSPHORUS","POTASSIUM","SODIUM","ZINC","ZINC","COPPER","MANGANESE","ALPHA-TOCOPHEROL",
					"BETA-TOCOPHEROL","GAMMA-TOCOPHEROL","DELTA-TOCOPHEROL","VITAMIN C","THIAMIN","RIBOFLAVIN","NIACIN (NICOTINIC ACID) PREFORMED","PANTOTHENIC ACID","VITAMIN B-6","CHOLINE, TOTAL",
					"BETAINE","ASPARTAME","ALPHA-TOCOPHEROL, ADDED","CHOLESTEROL","TOTAL PLANT STEROL","STIGMASTEROL","CAMPESTEROL","BETA-SITOSTEROL","LYCOPENE","BETA CAROTENE",
					"NATURALLY OCCURRING FOLATE","SELENIUM","RETINOL","RETINOL ACTIVITY EQUIVALENTS","BETA CAROTENE","ALPHA CAROTENE","ALPHA-TOCOPHEROL","VITAMIN D (INTERNATIONAL UNITS)",
					"VITAMIN D2, ERGOCALCIFEROL","VITAMIN D (D2 + D3)","BETA CRYPTOXANTHIN","LYCOPENE","LUTEIN AND ZEAXANTHIN","BIOTIN","TOTAL FOLACIN","VITAMIN B-12","VITAMIN K","FOLIC ACID","NATURALLY OCCURRING FOLATE"
					,"DIETARY FOLATE EQUIVALENTS"};
		    for (String key : compound) {
		        if (totalPeriodNutrient.containsKey(key)) {
		            totalPeriodNutrient.put(key, totalPeriodNutrient.get(key) / 1000);
		        }
		    }
		}
	//calculate number of days between 2 dates
	public static long daysBetween(String date1, String date2) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        LocalDate startDate = LocalDate.parse(date1, formatter);
        LocalDate endDate = LocalDate.parse(date2, formatter);
        return ChronoUnit.DAYS.between(startDate, endDate);
    }
	
	
	
//	public static Map<String, Double> calculateTotalNutrients(List<Map<String, String>> takeIn, IGetNutrientData data) {
//	    Map<String, Double> result = new HashMap<>();
//	    for (Map<String, String> food : takeIn) {
//	        double amount = Double.parseDouble(food.get("Amount"));
//	        int foodID = Integer.parseInt(food.get("FoodID"));
//	        List<Map<String, String>> nutrients = data.getFoodData(foodID);
//	        for (Map<String, String> nutrient : nutrients) {
//	            double nutrientValuePerGram = Double.parseDouble(nutrient.get("NutrientValue"));
//	            String nutrientID = nutrient.get("NutrientID");
//	            double totalNutrientValue = amount * nutrientValuePerGram;
//	            result.put(nutrientID, result.getOrDefault(nutrientID, 0.0) + totalNutrientValue);
//	        }
//	    }
//	    return result;
//	}


	
	public static void main(String[] args) throws Exception {
		IManageUserData user = new ManageUserDataMySQL();
		user.setUser("123", "123");
		 
		
		
//		List<Map<String, String>> meals = user.getUserMeals();
//		System.out.println("meals:"+meals);
//		List<String> mealIDs = getMealIDs(meals,"2023-10-13","2023-10-17");
//		System.out.println("mealIDs:"+mealIDs);
//		
		List<Map<String, String>> Ingredients=user.getUserMealIngredients();
		//System.out.println("Ingredients:"+Ingredients);
		String startDate="2023-10-17";
		String endDate="2023-10-22";
		Map<String, Double> periodNutrient=visualizeNutrientInPeriod(user,startDate,endDate);
		System.out.println("average nutrient breakdown during "+startDate+" and "+endDate+"\n" +periodNutrient );
		
		IGetNutrientData data=new NutrientData(new NutrientDataMySQL());
       // List<Map<String, String>>nu=data.getFoodData(3375);
       // System.out.println("nutrient of 3375:"+nu);
       
        user.close();
		System.out.println("done");
		
//		SwingUtilities.invokeLater(() -> {
//            JFrame frame = new JFrame("Simple Swing Example");
//            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//            frame.setSize(300, 200);
//
//            JButton button = new JButton("Click me!");
//            frame.getContentPane().add(button);
//
//            frame.setVisible(true);
//        });
	}
}

class PieCompare extends JFrame {
    public PieCompare() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(1360, 900); 
        setLayout(new GridLayout(2, 1)); 
    }

    public void visualize(Map<String, Double> top5, Map<String, Double> top10) {
        ChartPanel panel1 = createChartPanel(top5, "Top 5 Nutrients");
        ChartPanel panel2 = createChartPanel(top10, "Top 10 Nutrients");

        add(panel1);
        add(panel2);

        setVisible(true);
    }

    private ChartPanel createChartPanel(Map<String, Double> data, String title) {
        DefaultCategoryDataset dataset = new DefaultCategoryDataset();

        for (Map.Entry<String, Double> entry : data.entrySet()) {
            dataset.addValue(entry.getValue(), entry.getKey(), title);
        }

        JFreeChart chart = ChartFactory.createMultiplePieChart3D(title, dataset, TableOrder.BY_COLUMN,
                true, true, false);

        MultiplePiePlot plot = (MultiplePiePlot) chart.getPlot();
        JFreeChart subchart = plot.getPieChart();
        PiePlot p = (PiePlot) subchart.getPlot();
        p.setLabelGenerator(
                new StandardPieSectionLabelGenerator("{0} : ({2})", new DecimalFormat("0"), new DecimalFormat("0%")));
        p.setSectionPaint("Vegetable", new Color(157, 193, 131));
        p.setSectionPaint("Grains", new Color(230, 223, 0));
        p.setSectionPaint("Milk", new Color(135, 206, 250));
        p.setSectionPaint("Meat", new Color(254, 57, 57));
        p.setSectionPaint("Unknown", Color.BLACK);

        return new ChartPanel(chart);
    }
}





class PieChart extends JFrame {

    public PieChart() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(800, 400);
    }

    public void visualize(Map<String, Double> avgPeriodNutrient1, Map<String, Double> avgPeriodNutrient2) {
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(1, 2));

        panel.add(createChartPanel(avgPeriodNutrient1));
        panel.add(createChartPanel(avgPeriodNutrient2));

        setContentPane(panel);
        setVisible(true);
    }

    private ChartPanel createChartPanel(Map<String, Double> avgPeriodNutrient) {
        DefaultPieDataset dataset = new DefaultPieDataset();
        for (Map.Entry<String, Double> entry : avgPeriodNutrient.entrySet()) {
            dataset.setValue(entry.getKey(), entry.getValue());
        }

        JFreeChart chart = ChartFactory.createPieChart(
                "avgNutrient Distribution during this period",   // chart title
                dataset,          // data
                true,             // include legend
                true,
                false);

        PiePlot plot = (PiePlot) chart.getPlot();
        plot.setLabelGenerator(new StandardPieSectionLabelGenerator(
            "{0} : ({2})", new DecimalFormat("0.00"), new DecimalFormat("0.00%")));

        return new ChartPanel(chart);
    }
}