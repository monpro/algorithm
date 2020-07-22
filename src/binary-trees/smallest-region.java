import java.util.*;

class Solution {
    public String findSmallestRegion(List<List<String>> regions, String region1, String region2) {
        Map<String, String> childToParents = new HashMap<>();
        Set<String> visited = new HashSet<>();
        
        for(List<String> list: regions){
            String parent = list.get(0);
            for(int i = 1; i < list.size(); i++){
                childToParents.put(list.get(i), parent);
            }
        }
        
        while(region1 != null){
            visited.add(region1);
            region1 = childToParents.get(region1);
        }
        
        while(!visited.contains(region2)){
            region2 = childToParents.get(region2);
        }
        
        return region2;
    }
}