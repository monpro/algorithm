package designs;

import java.util.*;

class TimeDate {
    String value;
    int timestamp;
    
    public TimeDate(String val, int time){
        this.value = val;
        this.timestamp = time;
    } 
}

class TimeMap {

    /** Initialize your data structure here. */
    Map<String, List<TimeDate>> map;
    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        map.putIfAbsent(key, new ArrayList<>());
        map.get(key).add(new TimeDate(value, timestamp));
    }
    
    public String get(String key, int timestamp) {
        if(!map.containsKey(key)){
            return "";
        }
        
        List<TimeDate> list = map.get(key);
        
        int start = 0, end = list.size() - 1;
        
        while(start + 1 < end){
            int mid = start + (end - start) / 2;
            if(list.get(mid).timestamp == timestamp){
                return list.get(mid).value;
            }else if(list.get(mid).timestamp < timestamp){
                start = mid + 1;
            }else{
                end = mid - 1;
            }
        }
        if(list.get(end).timestamp <= timestamp){
            return list.get(end).value;
        }
        else if(list.get(start).timestamp <= timestamp){
            return list.get(start).value;
        }else{
            return "";
        }
    }
}
