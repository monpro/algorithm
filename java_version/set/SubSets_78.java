package set;

import java.util.ArrayList;
import java.util.List;

public class SubSets_78 {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if(nums.length == 0){
            return result;
        }
        helper(nums, result, new ArrayList<>(), 0);
        return result;
    }

    private void helper(int[] nums, List<List<Integer>> result, List<Integer> temp, int index){
        if(index == nums.length){
            result.add(new ArrayList<>(temp));
            return;
        }

        temp.add(nums[index]);
        helper(nums, result, temp, index + 1);
        temp.remove(temp.size() - 1);
        helper(nums, result, temp, index + 1);

    }

}
