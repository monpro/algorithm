package designs;

import java.util.*;

class LogSystem {
    List<String[]> storage;
    Map<String, Integer> map;
    public LogSystem() {
        storage = new ArrayList<>();
        map = new HashMap<>();
        map.put("Year", 4);
        map.put("Month", 7);
        map.put("Day", 10);
        map.put("Hour", 13);
        map.put("Minute", 16);
        map.put("Second", 19);
        
    }
    
    public void put(int id, String timestamp) {
        storage.add(new String[]{Integer.toString(id), timestamp});
    }
    
    public List<Integer> retrieve(String s, String e, String gra) {
        List<Integer> result = new ArrayList<>();
        int id = map.get(gra);
        for(String[] string: storage){
            String time = string[1].substring(0, id);
            
            if(time.compareTo(s.substring(0, id)) >= 0 && time.compareTo(e.substring(0, id)) <= 0){
                result.add(Integer.valueOf(string[0]));
            }
        }
        
        return result;
    }
}