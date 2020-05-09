import java.util.*;

class FirstKMissingPositive {

  public static List<Integer> findNumbers(int[] nums, int k) {
    List<Integer> missingNumbers = new ArrayList<>();
    int index = 0;
    while(index < nums.length){
      if(nums[index] > 0 && nums[index] <= nums.length && nums[index] != nums[nums[index] - 1]){
        swap(nums, index, nums[index] - 1);
      }else{
        index += 1;
      }
    }

    Set<Integer> existed = new HashSet<>();
    for(int i = 0; i < nums.length && missingNumbers.size() < k; i++){
      if(nums[i] != i + 1){
        missingNumbers.add(i + 1);
        existed.add(nums[i]);
      }
    }

    for(int i = 1; missingNumbers.size() < k; i++){
      int num = i + nums.length;
      if(!existed.contains(num)){
        missingNumbers.add(num);
      }
    }
    return missingNumbers;
  }

  public static void swap(int[] array, int i, int j){
    int temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
}