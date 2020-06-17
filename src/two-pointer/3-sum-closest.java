class Solution {
    public int threeSumClosest(int[] arr, int targetSum) {
        int smallestDiff = Integer.MAX_VALUE;
        Arrays.sort(arr);
        for(int i = 0; i < arr.length - 2; i++){
          if(i > 0 && arr[i - 1] == arr[i]){
            continue;
          }
          int left = i + 1, right = arr.length - 1;
          while(left < right){
            int temp = arr[i] + arr[left] + arr[right];

            if(temp - targetSum == 0){
              return targetSum;
            }
            else if(temp - targetSum > 0){
              right -= 1;
            }
            else{
              left += 1;
            }
            if(Math.abs(targetSum - temp) < Math.abs(smallestDiff)){
              smallestDiff = targetSum - temp;
            }
          }
        }
        return targetSum - smallestDiff;
    }
}