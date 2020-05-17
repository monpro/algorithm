package history.permutation;

import java.util.*;

class SubsetWithDuplicates {

    public static List<List<Integer>> findSubsets(int[] nums) {
        List<List<Integer>> subsets = new ArrayList<>();
        Arrays.sort(nums);

        subsets.add(new ArrayList<>());
        int startIndex = 0, endIndex = 0;

        for (int i = 0; i < nums.length; i++) {
            startIndex = 0;
            if (i > 0 && nums[i] == nums[i - 1]) {
                startIndex = endIndex;
            }
            endIndex = subsets.size();
            for (int j = startIndex; j < endIndex; j++) {
                List<Integer> subset = new ArrayList<>(subsets.get(j));
                subset.add(nums[i]);
                subsets.add(subset);
            }
        }
        return subsets;
    }

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums.length == 0)
            return result;
        Arrays.sort(nums);
        helper(result, new ArrayList<>(), nums, 0);
        return result;
    }

    private void helper(List<List<Integer>> result, List<Integer> subset, int[] nums, int position) {
        result.add(new ArrayList<>(subset));

        for (int i = position; i < nums.length; i++) {
            if (i > position && nums[i - 1] == nums[i])
                continue;
            subset.add(nums[i]);
            helper(result, subset, nums, i + 1);
            subset.remove(subset.size() - 1);
        }
    }
}