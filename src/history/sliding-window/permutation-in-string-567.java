class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s2.length() < s1.length())
            return false;
        
        int[] count = new int[26];
        for(int i = 0; i < s1.length(); i++){
            count[s1.charAt(i) - 'a'] += 1;
        }
        
        int left = 0, right = 0, num = s1.length();
        
        while(right < s1.length()){
            if(count[s2.charAt(right) - 'a'] > 0){
                num -= 1;
            }
            count[s2.charAt(right) - 'a'] -= 1;
            right += 1;
        }
        
        while(right < s2.length() && num != 0){
            
            count[s2.charAt(left) - 'a'] += 1;
            if(count[s2.charAt(left) - 'a'] > 0){
                num += 1;
            }
            
            if(count[s2.charAt(right) - 'a'] > 0){
                num -= 1;
            }
            count[s2.charAt(right) -'a'] -= 1;

            left += 1;
            right += 1;
        }
        return num == 0;
    }
}