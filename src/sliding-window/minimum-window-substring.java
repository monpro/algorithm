class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> map = new HashMap<>();
        for(char c: s.toCharArray()){
            map.put(c, 0);
        }
        for(char c: t.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        
        int left = 0, right = 0, count = t.length();
        int maxVal = Integer.MAX_VALUE;
        String result = "";
        
        while(right < s.length()){
            if(map.get(s.charAt(right)) > 0)
                count -= 1;
            map.put(s.charAt(right), map.get(s.charAt(right)) - 1);
            right += 1;
            while(count == 0){
                if(right - left < maxVal){
                    maxVal = right - left;
                    result = s.substring(left, right);
                }
                map.put(s.charAt(left), map.get(s.charAt(left)) + 1);
                if(map.get(s.charAt(left)) > 0)
                    count += 1;
                left += 1;
            }
        }
        if(maxVal == Integer.MAX_VALUE){
            return "";
        }else{
            return result;
        }
    }
}