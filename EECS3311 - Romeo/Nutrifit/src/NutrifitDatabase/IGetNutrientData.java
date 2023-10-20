package NutrifitDatabase;
import java.util.List;
import java.util.Map;

/**
 * This API gets data from the CanadianNutrientDB database.
 * @author Joshua Chen
 *
 */
public interface IGetNutrientData {
	
	/**
	 * to get the FoodID of a desired food look through the Food Name csv file in the Canadian Nutrient database on eclass
	 * @param FoodID
	 * @return
	 * @throws Exception
	 */
	public List<Map<String, String>> getFoodData(int FoodID);
}
