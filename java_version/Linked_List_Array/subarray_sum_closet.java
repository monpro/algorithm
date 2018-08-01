package Linked_List_Array;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/*
首先遍历整个数组获取prefixSum.
在获取prefixSum的时候，用HashMap来存Sum -> Index关系。
将prefixSum进行排序。
然后在排好序后找diff最小的两个值，
利用这两个值来获取原来的prefix的index即可。
 */
public class subarray_sum_closet {
    public int[] subarraySumClosest(int[] nums) {
        int[] result = new int[]{0,0};
        if(nums == null|| nums.length == 0){
            return result;
        }

        int[] prefix = new int[nums.length + 1];
        prefix[0] = 0;
        Map<Integer, Integer> sumToIndex = new HashMap<>();
        sumToIndex.put(0,0);
        for(int i = 0; i < nums.length;i++){
            prefix[i + 1] = prefix[i] + nums[i];
            if(sumToIndex.containsKey(prefix[i + 1])){
                result[0] = sumToIndex.get(prefix[i + 1]);
                result[1] = 1;
                return result;
            }
            else{
                sumToIndex.put(prefix[i + 1], i);
            }
        }
        Arrays.sort(prefix);
        int minDiff = Integer.MAX_VALUE, leftSum = -1, rightSum = -1;
        for(int i = 0; i < prefix.length - 1; i++){
            if(prefix[i + 1] - prefix[i] < minDiff){
                minDiff = prefix[i + 1] - prefix[i];
                leftSum = prefix[i];
                rightSum = prefix[i + 1];

            }
        }
        int leftIndex = sumToIndex.get(leftSum);
        int rightIndex = sumToIndex.get(rightSum);

        result[0] = Math.min(leftIndex, rightIndex) + 1;
        result[1] = Math.max(leftIndex,rightIndex);

        return result;

    }
}
