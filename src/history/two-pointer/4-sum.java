class Solution {
    public List<List<Integer>> fourSum(int[] arr, int target) {
        List<List<Integer>> quadruplets = new ArrayList<>();
        Arrays.sort(arr);
        for(int i = 0; i < arr.length - 3; i++){
          if(i > 0 && arr[i] == arr[i - 1]){
            continue;
          }
          for(int start = i + 1; start < arr.length - 2; start ++){
            if(start > i + 1 && arr[start] == arr[start - 1]){
              continue;
            }
            int val = target - arr[i] - arr[start];
            int left = start + 1, right = arr.length - 1;
            while(left < right){
              int temp = arr[left] + arr[right];
              if(temp == val){
                quadruplets.add(Arrays.asList(arr[i], arr[start], arr[left], arr[right]));
                left += 1;
                right -= 1;
                while(left < right && arr[left] == arr[left - 1]){
                  left += 1;
                }
                while(left < right && arr[right] == arr[right + 1]){
                  right -= 1;
                }
              }
              else if(temp < val){
                left += 1;
              }
              else{
                right -= 1;
              }
            }
          }
        }
        return quadruplets;
    }
}