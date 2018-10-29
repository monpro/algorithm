package dfs;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class subsets {

    public List<List<Integer>> subsets(int[] nums) {
        // write your code here
        Arrays.sort(nums);
        List<List<Integer>> results = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        helper(results, subset,nums, 0);
        return results;
    }

    void helper(List<List<Integer>> results, List<Integer> subset, int[] nums,int position) {
        if (position == nums.length) {
            results.add(new ArrayList<>(subset));
            return;
        }

        subset.add(nums[position]);
        helper(results,new ArrayList<>(subset),nums,position + 1);
        subset.remove(subset.size() - 1);
        helper(results,new ArrayList<>(subset),nums,position + 1);
    }
}
