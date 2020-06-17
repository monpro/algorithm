import java.util.*;

class Solution {
    public List<Integer> findSubstring(String str, String[] words) {
        List<Integer> resultIndices = new ArrayList<Integer>();
        if(str.length() == 0 || words.length == 0){
            return resultIndices;
        }
        Map<String, Integer> count = new HashMap<>();
        for(String word: words){
          count.put(word, count.getOrDefault(word, 0) + 1);
        }
        int length = words[0].length();
        int size = words.length;
        for(int start = 0; start <= str.length() - size * length; start++){
          Map<String, Integer> visited = new HashMap<>();
          for(int interval = 0; interval < size; interval++){
            int end = start + interval * length;
            String cur = str.substring(end, end + length);

            if(!count.containsKey(cur)){
              break;
            }

            visited.put(cur, visited.getOrDefault(cur, 0) + 1);
            if(visited.get(cur) > count.get(cur)){
              break;
            }
            if(interval + 1 == size){
              resultIndices.add(start);
            }
          }
        }

        return resultIndices;
    }
}