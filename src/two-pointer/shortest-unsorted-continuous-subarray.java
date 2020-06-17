class Solution {
    public int findUnsortedSubarray(int[] arr) {
        int left = 0, right = arr.length - 1;
        while(left < arr.length - 1 && arr[left] <= arr[left + 1]){
          left += 1;
        }
        if(left == arr.length - 1){
          return 0;
        }
        while(right > 0 && arr[right] >= arr[right - 1]){
          right -= 1;
        }

        int subArrayMax = Integer.MIN_VALUE, subArrayMin = Integer.MAX_VALUE;
        for(int i = left; i <= right; i++){
          subArrayMax = Math.max(arr[i], subArrayMax);
          subArrayMin = Math.min(arr[i], subArrayMin);
        }

        while(left > 0 && arr[left - 1] > subArrayMin){
          left -= 1;
        }

        while(right < arr.length - 1&& arr[right + 1] < subArrayMax){
          right += 1;
        }

        return right - left + 1;
    }
}