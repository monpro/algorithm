package permutation;

import java.util.*;

class Permutations {

    public static List<List<Integer>> findPermutations(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Queue<List<Integer>> queue = new LinkedList<>();
        queue.offer(new ArrayList<>());

        for (int num : nums) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                List<Integer> permutation = queue.poll();
                for (int j = 0; j <= permutation.size(); j++) {
                    List<Integer> newPermutation = new ArrayList<>(permutation);
                    newPermutation.add(j, num);

                    if (newPermutation.size() == nums.length) {
                        result.add(newPermutation);
                    } else {
                        queue.add(newPermutation);
                    }
                }
            }
        }
        return result;
    }

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        helper(results, new ArrayList<>(), nums, new boolean[nums.length]);
        return results;
    }

    void helper(List<List<Integer>> results, List<Integer> subset, int[] nums, boolean[] visited) {
        if (subset.size() == nums.length) {
            results.add(subset);
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (visited[i]) {
                continue;
            }
            subset.add(nums[i]);
            visited[i] = true;
            helper(results, new ArrayList<>(subset), nums, visited);
            visited[i] = false;
            subset.remove(subset.size() - 1);
        }
    }
}