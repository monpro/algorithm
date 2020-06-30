package dps;

class Solution {
    public int minCost(int[][] costs) {
        // ith house painted - i-1th house different color + color cost
        // dp[i][0] = min(dp[i - 1][1] + [0], dp[i - 1][2][0])
        int length = costs.length;
        int[][] dp = new int[costs.length + 1][3];
        
        for(int i = 1; i < costs.length + 1; i++){
            dp[i][0] = Math.min(dp[i - 1][1] + costs[i - 1][0], dp[i - 1][2] + costs[i - 1][0]);
            dp[i][1] = Math.min(dp[i - 1][0] + costs[i - 1][1], dp[i - 1][2] + costs[i - 1][1]);
            dp[i][2] = Math.min(dp[i - 1][0] + costs[i - 1][2], dp[i - 1][1] + costs[i - 1][2]);
        }
        
        return Math.min(Math.min(dp[length][0], dp[length][1]), dp[length][2]);
        
        
    }
}