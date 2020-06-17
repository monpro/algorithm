
import java.util.*;

class TripletWithSmallerSum {

  public static int searchTriplets(int[] arr, int target) {
    int count = 0;
    Arrays.sort(arr);
    for(int i = 0; i < arr.length - 2; i++){
      if(i > 0 && arr[i] == arr[i - 1]){
        continue;
      }
      int left = i + 1, right = arr.length - 1;
      while(left < right){
        int temp = arr[i] + arr[left] + arr[right];
        if(temp < target){
          count += right - left;
          left += 1;
        }
        else{
          right -= 1;
        }
      }
    }
    return count;
  }
}