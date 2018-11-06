package double_pointer;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class two_sum {
    public int[] twoSum(int[] numbers, int target) {
        /*
        numbers=[2, 7, 11, 15], target=9
        return [0, 1]
         */
        Map<Integer, Integer> map = new HashMap<>();
        if(numbers.length == 0){
            return new int[0];
        }
        int[] result = new int[2];
        for(int i = 0; i<numbers.length; i++){
            if(map.containsKey(numbers[i])){
                result[0] = map.get(numbers[i]);
                result[1] = i;
                return result;
            }
            map.put(target - numbers[i],i);
        }
        return result;
    }

    public int[] twoSum_pointer(int[] numbers, int target) {
        //how to use double pointer
        if(numbers.length == 0){
            return new int[0];
        }
        int[] result = new int[2];
        int left = 0, right =numbers.length - 1;
        int[] numbers_2 = Arrays.copyOf(numbers,numbers.length);
        int a = 0, b = 0;
        int i = 0;

        Arrays.sort(numbers_2);
        while (left < right){
            if(numbers_2[left] + numbers_2[right] < target){
                left++;
            }
            else if(numbers_2[left] + numbers_2[right] > target){
                right--;
            }
            else if(numbers_2[left] + numbers_2[right] == target){
                a = numbers_2[left];
                b = numbers_2[right];
                break;
            }



        }

        if(a == b){
            for(i = 0; i < numbers.length;i++){
                if(numbers[i] == a){
                    result[0] = i;
                    break;
                }
            }
            for(int j = i + 1; j < numbers.length;j++){
                if(numbers[j] == b){
                    result[1] = j;
                    break;
                }
            }
        }

        if(a != b){
            for(i = 0; i <numbers.length;i++){
                if(numbers[i] == a){
                    result[0] = i;
                }
                if(numbers[i] == b){
                    result[1] = i;
                }
            }
        }

        Arrays.sort(result);
        return result;
    }
}
