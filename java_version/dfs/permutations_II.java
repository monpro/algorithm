package dfs;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class permutations_II {
    public List<List<Integer>> permuteUnique(int[] nums) {
        // write your code here
        Arrays.sort(nums);
        List<List<Integer>> results = new ArrayList<>();
        helper(results, new boolean[nums.length], new ArrayList<>(), nums);
        return results;
    }

    void helper(List<List<Integer>> results, boolean[] visited, List<Integer> subset, int[] nums){
        if(subset.size() == nums.length){
            results.add(subset);
            return;
        }

        for(int i= 0; i < nums.length;i++){
            if(visited[i]){
                continue;
            }
            if(i > 0 && nums[i - 1] == nums[i] && !visited[i -1]){
                continue;
            }
            visited[i] = true;
            subset.add(nums[i]);
            helper(results,visited,new ArrayList<>(subset),nums);
            visited[i] = false;
            subset.remove(subset.size() - 1);


        }

    }
}
