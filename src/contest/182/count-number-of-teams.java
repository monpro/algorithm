class Solution {
    public int numTeams(int[] rating) {
        int result = 0;
        int n = rating.length;
        for(int j = 0; j < n; j++){
            int leftSmaller = 0, leftLarger = 0;
            int rightSmaller = 0, rightLarger = 0;
            
            for(int i = 0; i < j; i++){
                if(rating[i] < rating[j]) leftSmaller += 1;
                else if(rating[i] > rating[j]) leftLarger += 1;
            }
            
            for(int k = j + 1; k < n; k++){
                if(rating[k] < rating[j]) rightSmaller += 1;
                else if(rating[k] > rating[j]) rightLarger += 1;
            }
            
            result += leftSmaller * rightLarger + leftLarger * rightSmaller;
        }
        
        return result;
    }
}