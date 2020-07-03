package dps;

class SubsetSum {

    static boolean canPartition(int[] num, int sum) {
      // dp[i][s] - array[0...i] contain the subset sum s 
      boolean[][] dp = new boolean[num.length][sum + 1];
      int n = num.length;
      for(int i = 0; i < n; i++){
        dp[i][0] = true;
      }
  
      for(int i = 0; i <= sum; i++){
        if(num[0] == i){
          dp[0][i] = true;
        }
      }
  
      for(int i = 1; i < n; i++){
        for(int j = 1; j <= sum; j++){
          if(dp[i - 1][j]){
            dp[i][j] = dp[i - 1][j];
          }else if(j >= num[i]){
            dp[i][j] = dp[i - 1][j - num[i]];
          }
        }
      }
  
      return dp[n - 1][sum];
    }
  }