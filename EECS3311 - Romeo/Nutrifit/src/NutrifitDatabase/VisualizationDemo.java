package NutrifitDatabase;

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;
import java.awt.BorderLayout;
import java.awt.Color;

import javax.swing.JPanel;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.axis.ValueAxis;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.StandardXYItemRenderer;
import org.jfree.chart.ui.ApplicationFrame;
import org.jfree.data.general.AbstractDataset;
import org.jfree.data.time.Day;
import org.jfree.data.time.TimeSeries;
import org.jfree.data.time.TimeSeriesCollection;


abstract class DataSchema{
	Dataset data;
	String name;
	DataSchema(Dataset data, String name){
		this.data = data;
		this.name = name;
	}
	
	abstract AbstractDataset getDataSchema(String from, String to);
}

class TimeSeriesSchema extends DataSchema{
	TimeSeriesSchema(Dataset data, String name){
		super(data, name);
	}
	
	@Override
	AbstractDataset getDataSchema(String from, String to) {
		TimeSeries timeSeries = new TimeSeries(this.name);
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-mm-dd");
    	Date fromDate = null;
    	Date toDate = null; 
    	
    	try {
    		fromDate = sdf.parse(from);
    		toDate = sdf.parse(to);
    	}catch(Exception e) {}
    	
		for(Map<String, String> rec: data.getData()) {
			try {
				Date curDate = sdf.parse(rec.get("Date"));
				if(curDate.compareTo(fromDate) >= 0 && curDate.compareTo(toDate) <= 0) {
		        	timeSeries.add(Day.parseDay(rec.get("Date")), Double.valueOf(rec.get("Value")));
				}
		    }catch(Exception e) {}
		}
		
		return new TimeSeriesCollection(timeSeries);
	}
}


abstract class Dataset{
	List<Map<String, String>> data;
	
	Dataset(List<Map<String, String>> data){
		this.data = data;
	}
	
	abstract void setUserData(IManageUserData user);
	
	List<Map<String, String>> getData(){
		return this.data;
	}
	
	static void groupSummingDouble(List<Map<String, String>> into ,List<Map<String, String>> container, String accumulator, String groupBy) {
		container.stream().collect(Collectors.groupingBy(tuple -> tuple.get(groupBy), 
				Collectors.summingDouble(tuple -> Double.valueOf(tuple.get(accumulator))))).forEach((date, value) ->{
					Map<String, String> map = new HashMap<>();
					map.put("Date", date);
					map.put("Value", String.valueOf(value));
					into.add(map);
				});
	}
}



class CaloryIntakeDataset extends Dataset{
	
	public CaloryIntakeDataset() {
		super(new ArrayList<>());
	}
	
	@Override
	void setUserData(IManageUserData user) {
		this.data.clear();
		List<Map<String, String>> meals = user.getUserMeals();
		List<Map<String, String>> mealFood = user.getUserMealIngredients();
		List<Map<String, String>> mealCalories = new ArrayList<>();
		
		for(Map<String, String> mealRecord: meals) {
			List<Map<String, String>> caloriesMeal = mealFood.stream().
			filter(tuple -> tuple.get("MealID").equals(mealRecord.get("MealID"))).
			collect(Collectors.toList());
			
			double calories = CalculationsUtilities.getMealCalories(caloriesMeal);
			mealRecord.put("CaloryIntake", String.valueOf(calories));
			mealCalories.add(mealRecord);
		}
		
		Dataset.groupSummingDouble(this.data, mealCalories, "CaloryIntake", "Date");
	}
}

class CaloriesBurntDataset extends Dataset{
	
	public CaloriesBurntDataset(){
		super(new ArrayList<>());
	}
	
	@Override
	public void setUserData(IManageUserData user) {
		this.data.clear();
		List<Map<String, String>> exercises = user.getUserExercises();
		List<Map<String, String>> caloriesBurnt = new ArrayList<>();
		double weight = Double.valueOf(user.getProfileData().get("Weight"));
		
		for(Map<String, String> exerciseRecord: exercises) {
			double calories = CalculationsUtilities.calculateCaloriesBurnt(exerciseRecord.get("Intensity"), 
					Double.valueOf(exerciseRecord.get("Duration")), weight);
			exerciseRecord.put("CaloriesBurnt", String.valueOf(calories));
			caloriesBurnt.add(exerciseRecord);
		}
		
		Dataset.groupSummingDouble(this.data, caloriesBurnt, "CaloriesBurnt", "DateTime");
	}
}

public class VisualizationDemo extends ApplicationFrame{
	private static final long serialVersionUID = 1L;
	
	/**
	 * 
	 * @param title title of the frame
	 * @param chart chart type
	 * @throws Exception
	 */
    public VisualizationDemo(final String title, JFreeChart chart) throws Exception{
        super(title);
        JPanel content = new JPanel(new BorderLayout());
		ChartPanel chartPanel = new ChartPanel(chart);
      	content.add(chartPanel);
      
      	chartPanel.setPreferredSize(new java.awt.Dimension(700, 600));
      	setContentPane(content);
    }
    
	//testing purposes.
	public static void main(String[] args) throws Exception{
		IManageUserData user = new ManageUserDataMySQL();
		user.setUser("123", "123");
		
		Dataset caloriesIntake = new CaloryIntakeDataset();
		caloriesIntake.setUserData(user);
		DataSchema schema = new TimeSeriesSchema(caloriesIntake, "Calories consumed");
		
		Dataset caloriesBurnt = new CaloriesBurntDataset();
		caloriesBurnt.setUserData(user);
		DataSchema schema2 = new TimeSeriesSchema(caloriesBurnt, "Calories burnt");
		
		JFreeChart chart = ChartFactory.createTimeSeriesChart(
	          "Calories consumed vs Calories burnt", "Date", "Calories(kJ)", 
	          (TimeSeriesCollection)schema.getDataSchema("2023-10-15", "2023-10-28"), true, true, false
	      );
		
		XYPlot plot = chart.getXYPlot();
		plot.setBackgroundPaint(Color.lightGray);
		plot.setDomainGridlinePaint(Color.white);
		plot.setRangeGridlinePaint(Color.white);
		
		final ValueAxis axis = plot.getDomainAxis();
		axis.setAutoRange(true);
		
		plot.setDataset(2, (TimeSeriesCollection)schema2.getDataSchema("2023-10-15", "2023-10-28"));
		plot.setRenderer(2, new StandardXYItemRenderer());
		
		VisualizationDemo demo = new VisualizationDemo("Deliverable1", chart);
		
		demo.pack();
		demo.setVisible(true);
		
		user.close();
	}
}
