package history.permutation;

import java.util.*;

class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode(int x) {
    val = x;
  }
};
class Solution {
    Map<Integer, Integer> cache = new HashMap<>();
    public int numTrees(int n) {  
        //dp[n] means when n become the root, how many bst will be? 
        if(n <= 1){
            return 1;
        }
        if(cache.containsKey(n)){
            return cache.get(n);
        }
        int count = 0;
        for(int i = 1; i <= n; i++){
          int leftTree = numTrees(i - 1);
          int rightTree = numTrees(n - i);
          
          count += leftTree * rightTree;
        }
        cache.put(n, count);
        return count;
    }

    public int numTreesDp(int n) {  
        int[] dps = new int[n + 1];
        dps[0] = 1;
        dps[1] = 1;
        for(int i = 2; i <= n; i++){
            for(int j = 0; j < i; j++){
                dps[i] += dps[i - j - 1] * dps[j];
            } 
        }
        return 0;

    }
}