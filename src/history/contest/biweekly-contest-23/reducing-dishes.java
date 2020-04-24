class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        int result = 0, total = 0;
        int n = satisfaction.length;
        Arrays.sort(satisfaction);
        // say:
        //[-1,-8,0,5,-9] -sort- [-9, -8, -1, 0, 5]
        // total + s[i]: 5 result 5
        // total + s[i]: 5 result 10
        // total + s[i]: 4 result 14   
        // total + s[i]:-4 result 14
        // total + s[i]: -13 result 14
        //so start from the most satisfied value, this value will accumlated during loop  += total
        //once the dish cannot contribute to the result, then skip it  total + satisfaction[i] >= 0
        for(int i = n - 1; i >= 0 && total + satisfaction[i] >= 0 ; i--){
            total += satisfaction[i];
            result += total;
        }
        
        return result;
    }
}