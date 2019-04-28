package tree;

public class UniqueBinarySearchTree {
    public int numTrees(int n) {
        //dp[n] means when n become the root, how many bst will be?
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for(int i = 2; i <= n; i++){
            for(int j = 0; j < i; j++){
                dp[i] += dp[j] * dp[i - j - 1];
            }
        }
        return dp[n];
    }
}
