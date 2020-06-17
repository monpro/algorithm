class Solution {
    public int longestOnes(int[] arr, int k) {
        int start = 0, result = 0;
        int count = 0;

        for(int end = 0; end < arr.length; end++){
          if(arr[end] == 0){
            count += 1;
          }

          while(count > k){
            if(arr[start] == 0){
              count -= 1;
            }
            start += 1;
          }
          result = Math.max(result, end - start + 1);
        }

        return result;
    }
}