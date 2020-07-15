import java.util.*;

class Solution {
    
    final double eps = 0.001;
    public boolean judgePoint24(int[] nums) {
        List<Double> arr = new ArrayList<>();
        for(int n : nums){
            arr.add((double) n);
        }
        
        return backtrace(arr);
        
    }
    
    
    public boolean backtrace(List<Double> arr){
        if(arr.size() == 1){
            if(Math.abs(arr.get(0) - 24.0) < eps){
                return true;
            }
            return false;
        }
        
        int size = arr.size();
        for(int i = 0; i < size; i++){
            for(int j = i + 1; j < size; j++){
                List<Double> next = new LinkedList<>();
                for(int k = 0; k < size; k++){
                    if(k != i && k != j){
                        next.add(arr.get(k));
                    }
                }
                
                // get possible computes and do backtrace
                for(double compute: getComputes(arr.get(i), arr.get(j))){
                    next.add(compute);
                    if(backtrace(next)){
                        return true;
                    }
                    next.remove(next.size() - 1);
                }
                
            }
        }
        
        return false;
    }
    
    public List<Double> getComputes(double a, double b){
        List<Double> result = Arrays.asList(a + b, a - b, b - a, a * b, a / b, b / a);
        return result;
    }
}