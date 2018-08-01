package dfs;

import org.omg.Messaging.SYNC_WITH_TRANSPORT;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

public class combinationSum2 {
    public List<List<Integer>> combinationSum2(int[] num, int target) {
        List<List<Integer>> results = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        Arrays.sort(num);

        helper(results, subset, num,target,0);
        return results;
    }
    void helper(List<List<Integer>> results, List<Integer> subset, int[] num, int target, int position){
        if(target == 0){
            results.add(new ArrayList<>(subset));
        }

        for(int i = position; i < num.length;i++){
            if(i != position && num[i] == num[i - 1]){
                continue;
            }
            subset.add(num[i]);
            helper(results,new ArrayList<>(subset),num,target - num[i], i + 1);
            subset.remove(subset.size() - 1);
        }

    }

//    int[] remove_duplicated(int[] subset){
//        int[] new_subset = new int[subset.length];
//        int count = 0;
//        for(int i=0 ; i < subset.length; i++){
//            int var = subset[i];
//            if(IntStream.of(new_subset).anyMatch(x -> x == var)){
//                continue;
//            }
//            new_subset[count] = var;
//            count += 1;
//        }
//        return new_subset;
//
//
//    }
}
