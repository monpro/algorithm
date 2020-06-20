package strings;

class Solution {
    public boolean repeatedSubstringPattern(String s) {
        if(s==null || s.length()<=1) return false;
        int length = s.length();
        for(int i = 1;i <= length / 2; i++){
            if(length % i != 0){
                continue;
            }
            String repeat = s.substring(0, i);
            for(int j = 0; j <= length; j+= repeat.length()){
                if(j == length){
                    return true;
                }
                if(!s.startsWith(repeat, j)){
                    break;
                }

            }
        }
        return false;
    }

}