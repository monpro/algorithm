import java.util.HashMap;
import java.util.Map;

class Solution {
    public int subarraysWithKDistinct(int[] A, int K) {
        return atMostK(A, K) - atMostK(A, K - 1);
    }
    
    public int atMostK(int[] A, int K){
        int left = 0, result = 0;
        Map<Integer, Integer> count = new HashMap<>();
        for(int right = 0; right < A.length; right++){
            if(count.getOrDefault(A[right], 0) == 0)
                K -= 1;
            count.put(A[right], count.getOrDefault(A[right], 0) + 1);
            while(K < 0){
                count.put(A[left], count.getOrDefault(A[left], 0) - 1);
                if(count.get(A[left]) == 0)
                    K += 1;
                left += 1;
            }
            
            result += right - left + 1;
        }
        
        return result;
    }

}