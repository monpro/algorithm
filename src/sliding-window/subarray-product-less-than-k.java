import java.util.*;

class Solution {
    public int numSubarrayProductLessThanK(int[] arr, int k) {
        int product = 1, left = 0;
        int count = 0;
        for(int right = 0; right < arr.length; right++){
            product *= arr[right];
            
            while(product >= k && left <= right){
                product /= arr[left++];
            }
            
            count += right - left + 1;
        }
        return count;
    }

    public static List<List<Integer>> findSubarrays(int[] arr, int target) {
        List<List<Integer>> subarrays = new ArrayList<>();
        int left = 0, product = 1;
        for(int right = 0; right < arr.length; right++){
          product *= arr[right];
          while(product >= target && left <= right){
            product /= arr[left++];
          }
          List<Integer> temp = new ArrayList<>();
          for(int i = right; i >= left; i--){
            temp.add(0, arr[i]);
            subarrays.add(new ArrayList<>(temp));
          }
        }
        return subarrays;
      }
}