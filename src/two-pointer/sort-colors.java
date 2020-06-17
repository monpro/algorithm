class Solution {
    public void sortColors(int[] arr) {
        int left = 0, right = arr.length - 1;
        int cur = 0;
        while(cur <= right){
          if(arr[cur] == 0){
            swap(arr, cur, left);
            cur += 1;
            left += 1;
          }
          else if(arr[cur] == 1){
            cur += 1;
          }
          else if(arr[cur] == 2){
            swap(arr, cur, right);
            right -= 1;
          }
        }
  }

  private void swap(int[] arr, int i, int j){
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }
}