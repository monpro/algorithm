package dps;

class PartitionSet {
    public int canPartition(int[] num) {
      int sum = 0;
      for (int i = 0; i < num.length; i++)
        sum += num[i];
  
      int n = num.length;
      boolean[][] dp = new boolean[n][sum/2 + 1];
  
      // populate the sum=0 columns, as we can always form '0' sum with an empty set
      for(int i=0; i < n; i++)
        dp[i][0] = true;
  
      // with only one number, we can form a subset only when the required sum is equal to that number
      for(int s=1; s <= sum/2 ; s++) {
        dp[0][s] = (num[0] == s ? true : false);
      }
  
      // process all subsets for all sums
      for(int i=1; i < num.length; i++) {
        for(int s=1; s <= sum/2; s++) {
          // if we can get the sum 's' without the number at index 'i'
          if(dp[i-1][s]) {
            dp[i][s] = dp[i-1][s];
          } else if (s >= num[i]) {
            // else include the number and see if we can find a subset to get the remaining sum
            dp[i][s] = dp[i-1][s-num[i]];
          }
        }
      }
  
      int sum1 = 0;
      // Find the largest index in the last row which is true
      for (int i = sum / 2; i >= 0; i--) {
        if (dp[n-1][i] == true) {
            sum1 = i;
            break;
        }
      }
  
      int sum2 = sum - sum1;
      return Math.abs(sum2-sum1);
    }
  
    public static void main(String[] args) {
      PartitionSet ps = new PartitionSet();
      int[] num = {1, 2, 3, 9};
      System.out.println(ps.canPartition(num));
      num = new int[]{1, 2, 7, 1, 5};
      System.out.println(ps.canPartition(num));
      num = new int[]{1, 3, 100, 4};
      System.out.println(ps.canPartition(num));
    }
  }