class Solution {
    public int numberOfSubstrings(String s) {
        int[] count = {0, 0, 0};
        int left = 0, result = 0;
        for(int right = 0; right < s.length(); right++){
            count[s.charAt(right) - 'a'] += 1;
            while(count[0] > 0 && count[1] > 0 && count[2] > 0){
                count[s.charAt(left) - 'a'] -= 1;
                left += 1;
            }
            
            result += left;
        }
        
        return result;
    }
}