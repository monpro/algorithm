package Linked_List_Array;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class subarray_sum {
    public List<Integer> subarraySum(int[] nums) {
        // write your code here
        //Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
        Map<Integer, Integer> map = new HashMap<>();
        List<Integer> list = new ArrayList<>();
        //map is value - index
        map.put(0,-1);
        int sum = 0;
        for(int i = 0; i < nums.length;i++){
            sum += nums[i];
            if(map.containsKey(sum)){
                int digit = map.get(sum) + 1;
                list.add(digit);
                list.add(i);
                return list;
            }
            map.put(sum,i);
        }
        return list;
    }
}
