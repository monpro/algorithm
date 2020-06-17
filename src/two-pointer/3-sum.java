import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] arr) {
        List<List<Integer>> triplets = new ArrayList<>();
        for(int i = 0; i < arr.length - 2; i++){
          if(i > 0 && arr[i] == arr[i - 1]){
            continue;
          }
          Arrays.sort(arr);
          int left = i + 1, right = arr.length - 1;

          while(left < right){
            int temp = arr[i] + arr[left] + arr[right];
            if(temp == 0){
              triplets.add(Arrays.asList(arr[i], arr[left], arr[right]));
              left += 1;
              right -= 1;
              while(left < right && arr[left] == arr[left - 1]){
                left += 1;
              }
              while(left < right && arr[right] == arr[right + 1]){
                right -= 1;
              }
            }
            else if(temp > 0){
              right -= 1;
              while(left < right && arr[right] == arr[right + 1]){
                right -= 1;
              }
            }
            else{
              left += 1;
              while(left < right && arr[left] == arr[left - 1]){
                left += 1;
              }
            }
          }
        }
        return triplets;
    }
}