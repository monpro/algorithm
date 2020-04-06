class Solution {
    public int numTimesAllBlue(int[] light) {
        int result = 0, rightMost = 0;
        
        for(int i = 0; i < light.length; i++){
            rightMost = Math.max(light[i], rightMost);
            if(rightMost == i + 1)
                result += 1;
        }
        
        return result;
    }
}