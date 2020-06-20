package strings;

class Solution {
    public String shiftingLetters(String S, int[] shifts) {
        // shifts[index] = sum(shifts[index: -1])
        int length = shifts.length;
        if(length >= 2){
            // [3, 5, 9] -> [3 + (5 + 9), 5 + 9, 9]
            for(int i = length - 2; i >= 0; i--){
                shifts[i] = (shifts[i] + shifts[i + 1]) % 26;
            }
        }
        
        StringBuilder stringBuilder = new StringBuilder();
        for(int i = 0; i < length; i++){
            char ch = S.charAt(i);
            int offset = ch - 'a';
            offset = (offset + shifts[i]) % 26;
            
            ch = (char)('a' + offset);
            stringBuilder.append(ch);
        }
        
        return String.valueOf(stringBuilder);
        
    }
}