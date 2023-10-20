package NutrifitDatabase;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
/**
 * Retrieves data from the Canadian Nutrient file. Data from the nutrient file can be considered 
 * static so, a cache aside approach works well here.
 * @author Joshua Chen
 *
 */
public class NutrientData implements IGetNutrientData{

	private Map<Integer, List<Map<String, String>>> cache;
	private IGetNutrientData service;
	
	public NutrientData(IGetNutrientData service) {
		this.service = service;
		this.cache = new HashMap<>();
	}
	
	@Override
	public List<Map<String, String>> getFoodData(int FoodID){
		if(this.cache.containsKey(FoodID)) { //do I have this query?
			return this.cache.get(FoodID);
		}
		
		List<Map<String, String>> results = this.service.getFoodData(FoodID); //query database
		this.cache.put(FoodID, results); //memorize in cache
				
		
		return this.cache.get(FoodID);
	}
}
