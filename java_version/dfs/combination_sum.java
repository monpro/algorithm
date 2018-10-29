package dfs;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class combination_sum {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        // write your code here
        /*
        Given candidate set [2,3,6,7] and target 7, a solution set is:
        [7]
        [2, 2, 3]
        */
        Arrays.sort(candidates);
        List<List<Integer>> results = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        helper(results, subset, target, candidates,0);

        return results;

    }

    void helper(List<List<Integer>> results, List<Integer> subset, int target, int[] candidates, int position){
        if(target == 0){
            results.add(new ArrayList<>(subset));
            return;
        }
        if(position == candidates.length){
            return;
        }

        if(candidates[position] > target){
            return;
        }
        for(int i = position; i < candidates.length;i++){
            //reduce duplicates because candidates[i - 1] have been put into recursive
            if(i > 0 && candidates[i] == candidates[i -1]){
                continue;
            }
            subset.add(candidates[i]);
            helper(results, new ArrayList<>(subset), target - candidates[i], candidates, i);
            subset.remove(subset.size() - 1);

        }

    }

}
