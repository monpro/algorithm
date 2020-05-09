class FindCorruptNums {

    public static int[] findNumbers(int[] nums) {
      int index = 0;
      while(index < nums.length){
        int indexShouldAt = nums[index] - 1;
        if(nums[index] != nums[indexShouldAt]){
          swap(nums, index, indexShouldAt);
        }
        else{
          index += 1;
        }
      }
  
      for(int i = 0; i < nums.length; i++){
        if(nums[i] != i + 1){
          return new int[] {nums[i], i + 1};
        }
      }
      return new int[] { -1, -1 };
    }
  
    public static void swap(int[] array, int i, int j){
      int temp = array[i];
      array[i] = array[j];
      array[j] = temp;
    }
  }