class Solution {
    public boolean canConstruct(String s, int k) {
        int[] count = new int[26];
        for(int i = 0; i < s.length(); i++){
            count[s.charAt(i) - 'a'] += 1;
        }
        
        int oddNums = 0;
        for(int i : count){
            if(i % 2 == 1)
                oddNums += 1;
        }
        
        return oddNums <= k && k <= s.length();
    }
}