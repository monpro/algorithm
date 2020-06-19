class Solution {
    public int strongPasswordChecker(String s) {
        int lower = 0, upper = 0, digit = 0;
        char[] chars = s.toCharArray();
        for(char ch: chars){
            if(ch >= 'a' && ch <= 'z'){
                lower = 1;
            }
            else if(ch >= 'A' && ch <= 'Z'){
                upper = 1;
            }
            else if(Character.isDigit(ch) == true){
                digit = 1;
            }
        }
        int missingType = 3 - (lower + upper + digit);
        
        int change = 0;
        int oneDuplicate = 0, twoDuplicate = 0;
        int index = 2;
        
        while(index < chars.length){
            if(chars[index] == chars[index - 1] && chars[index - 1] == chars[index - 2]){
                int length = 2;
                
                while(index < chars.length && chars[index] == chars[index - 1]){
                    length += 1;
                    index += 1;
                }
                
                change += length / 3;
                if(length % 3 == 0){
                    oneDuplicate += 1;
                }
                if(length % 3 == 1){
                    twoDuplicate += 1;
                }
            }else{
                index += 1;
            }
        }
        
        if(chars.length < 6){
            return Math.max(missingType, 6 - s.length());
        }
        else if(chars.length <= 20){
            return Math.max(missingType, change);
        }else{
            int delete = chars.length - 20;
            change -= Math.min(delete, oneDuplicate);
            change -= Math.min(Math.max(delete - oneDuplicate, 0), twoDuplicate * 2) / 2;
            change -= Math.max(delete - oneDuplicate - 2 * twoDuplicate, 0) / 3;
            
            return delete + Math.max(missingType, change);
        }
        
    }
}