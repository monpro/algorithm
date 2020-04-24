class Solution {
    public int findMinMoves(int[] machines) {
        int sum = 0;
        for(int i: machines)
            sum += i;
        if(sum % machines.length != 0)
            return -1;
        int target = sum / machines.length, result = 0, tempSum = 0;
        
        for(int i = 0; i < machines.length; i++){
            tempSum += machines[i];
            
            result = Math.max(result, Math.abs(tempSum - (i + 1) * target));
            
            result = Math.max(result, machines[i] - target);
        }
        
        return result;
    }
}