package dfs;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class permutations {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        helper(results, new ArrayList<>(), nums, new boolean[nums.length]);
        return results;
    }

    void helper(List<List<Integer>> results, List<Integer> subset, int[] nums, boolean[] visited){
        if(subset.size() == nums.length){
            results.add(subset);
            return;
        }

        for(int i= 0; i < nums.length;i++){
            if(visited[i]){
                continue;
            }
            subset.add(nums[i]);
            visited[i] = true;
            helper(results, new ArrayList<>(subset),nums, visited);
            visited[i] = false;
            subset.remove(subset.size() - 1);
//            helper(results, new ArrayList<>(subset),nums,visited);
        }

    }
}
