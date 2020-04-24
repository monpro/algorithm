import java.util.Map;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        String str = s;
        Map<Character, Integer> visited = new HashMap<>();
        char[] array = str.toCharArray();
        int start = 0, result = 0;
        for(int end = 0; end < array.length; end++){
          if(visited.containsKey(array[end])){
            start = Math.max(start, visited.get(array[end]) + 1);
          }
          visited.put(array[end], end);
          result = Math.max(result, end - start + 1);
        }
        return result;
    }
}