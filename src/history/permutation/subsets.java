package history.permutation;

import java.util.*;

class Subsets {

    public static List<List<Integer>> findSubsets(int[] nums) {
        List<List<Integer>> subsets = new ArrayList<>();
        // start by adding the empty subset
        subsets.add(new ArrayList<>());
        for (int currentNumber : nums) {
            // we will take all existing subsets and insert the current number in them to
            // create new subsets
            int n = subsets.size();
            for (int i = 0; i < n; i++) {
                // create a new subset from the existing subset and insert the current element
                // to it
                List<Integer> set = new ArrayList<>(subsets.get(i));
                set.add(currentNumber);
                subsets.add(set);
            }
        }
        return subsets;
    }

    public List<List<Integer>> subsets(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> results = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        helper(results, subset, nums, 0);
        return results;
    }

    private void helper(List<List<Integer>> results, List<Integer> subset, int[] nums, int position) {
        if (position > nums.length)
            return;
        if (position == nums.length) {
            results.add(new ArrayList<>(subset));
            return;
        }
        subset.add(nums[position]);
        helper(results, subset, nums, position + 1);
        subset.remove(subset.size() - 1);
        helper(results, subset, nums, position + 1);
    }
}