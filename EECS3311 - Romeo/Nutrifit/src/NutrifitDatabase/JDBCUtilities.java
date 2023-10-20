package NutrifitDatabase;

import java.sql.Connection;
import org.apache.commons.dbcp2.BasicDataSource;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class JDBCUtilities {
	
	private static BasicDataSource dataSource;
	static {
		JDBCUtilities.dataSource = new BasicDataSource();
		JDBCUtilities.dataSource.setUrl("jdbc:mysql://192.186.116.212:3306");
		JDBCUtilities.dataSource.setUsername("NutrifitUser");
		JDBCUtilities.dataSource.setPassword("UserUser123!");
		
		
		JDBCUtilities.dataSource.setMinIdle(1);
		JDBCUtilities.dataSource.setMaxIdle(1);
	}
	
	static BasicDataSource getDataSource() {
		return JDBCUtilities.dataSource;
	}
	
	
	static void close(Connection connection, Statement statement, ResultSet set){
		try {
			if(connection != null) {
				connection.close();
			}
		}catch(SQLException e) {}
		
		try {
			if(statement != null) {
				statement.close();
			}
		}catch(SQLException e) {}
		
		try {
			if(set != null) {
				set.close();
			}
		}catch(SQLException e) {}
	}
	
	static List<Map<String, String>> extractResult(ResultSet set) throws SQLException{
		List<Map<String, String>> res = new ArrayList<>();
		
		while(set.next()) {
			Map<String, String> curMap = new HashMap<>();
					
			ResultSetMetaData metaData = set.getMetaData();
			for(int i = 1; i <= metaData.getColumnCount(); i ++) {
				String colName = metaData.getColumnName(i);
				String col = set.getString(colName);
				curMap.put(colName, col);
			}
			
			res.add(curMap);
		}
		
		return res;
	}
}
