package strings;

class Solution {
    public int shortestWay(String source, String target) {
        int tPoint = 0;
        int tempPoint = 0;
        
        int result = 0;
        while(tPoint < target.length()){
            tempPoint = tPoint;
            
            for(char ch: source.toCharArray()){
                if(tPoint < target.length() && ch == target.charAt(tPoint)){
                    tPoint += 1;
                }
            }
            
            if(tempPoint == tPoint){
                return -1;
            }
            
            result += 1;
        }
        
        return result;
    }
}