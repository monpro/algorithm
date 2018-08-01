package Linked_List_Array;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class intersection_of_two_arrays {
    public int[] intersection(int[] nums1, int[] nums2) {
        // write your code here
        /*
        Given two arrays, write a function to compute their intersection.
        Example
        Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
        Challenge
        Can you implement it in three different algorithms?
        Notice
        Each element in the result must be unique.
        The result can be in any order.
         */
        Map<Integer, Integer> map = new HashMap<>();
        Map<Integer,Integer> result = new HashMap<>();
        for(Integer i: nums1){
            if(!map.containsKey(i)){
                map.put(i,0);
            }
            else{
                map.put(i, map.get(i) + 1);
            }
        }
        for(Integer i : nums2){
            if(!result.containsKey(i)){
                result.put(i,0);
            }
            else{
                map.put(i, map.get(i) + 1);
            }
        }
        List<Integer> list = new ArrayList<>();
        for(Integer i: map.keySet()){
            if(result.containsKey(i) && map.containsKey(i)){
                list.add(i);
            }
        }
        int[] result_list = new int[list.size()];
        int count = 0;
        for(Integer i: list){
            result_list[count] = i;
            count += 1;
        }
        return result_list;
    }
}
