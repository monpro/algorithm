import java.util.*;

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] count = new int[26];
        for(int i = 0; i < p.length(); i++){
            count[p.charAt(i) - 'a'] += 1;
        }
        List<Integer> result = new ArrayList<>();
        for(int left = 0, right = 0; right < s.length(); right++){
            int rightPos = s.charAt(right) - 'a';
            count[rightPos] -= 1;
            
            while(count[rightPos] < 0){
                int leftPos = s.charAt(left) - 'a';
                count[leftPos] += 1;
                left += 1;
            }
            
            if(right - left + 1 == p.length()){
                result.add(left);
            }
            
        }
        return result;
    }
    public List<Integer> findAnagramsHash(String str, String pattern) {
        List<Integer> resultIndices = new ArrayList<Integer>();
        Map<Character, Integer> visited = new HashMap<>();
        for(char c: pattern.toCharArray()){
          visited.put(c, visited.getOrDefault(c, 0) + 1);
        }
        int start = 0, match = 0;
        char[] arr = str.toCharArray();
        for(int end = 0; end < arr.length; end++){
          if(visited.containsKey(arr[end])){
            visited.put(arr[end], visited.get(arr[end]) - 1);
            if(visited.get(arr[end]) == 0){
              match += 1;
            }
          }

          if(match == visited.size()){
            resultIndices.add(start);
          }

          if(end >= pattern.length() - 1){
            if(visited.containsKey(arr[start])){
              if(visited.get(arr[start]) == 0){
                match -= 1;
              }
              visited.put(arr[start], visited.get(arr[start]) + 1);
            }
            start += 1;
          }
        }
        return resultIndices;
    }
}