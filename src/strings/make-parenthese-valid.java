package strings;

class Solution {
    public int minAddToMakeValid(String S) {
        int leftBracket = 0, rightBracket = 0;
        for(char ch: S.toCharArray()){
            if(ch == '('){
                rightBracket += 1;
            }else if(ch == ')'){
                if(rightBracket == 0){
                    leftBracket += 1;
                }else{
                    rightBracket -= 1;
                }
            }
        }
        
        return leftBracket + rightBracket;
        
    }
}