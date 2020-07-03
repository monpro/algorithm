package dps;

class SubsetSum {
    static int countSubsets(final int[] num, final int sum) {
        final int[] dp = new int[sum + 1];
        dp[0] = 1;

        // with only one number, we can form a subset only when the required sum is
        // equal to its value
        for (int s = 1; s <= sum; s++) {
            dp[s] = (num[0] == s ? 1 : 0);
        }

        // process all subsets for all sums
        for (int i = 1; i < num.length; i++) {
            for (int s = sum; s >= 0; s--) {
                if (s >= num[i])
                    dp[s] += dp[s - num[i]];
            }
        }
        return dp[sum];
    }
  }
  