class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        coins = [1] + nums + [1]
        n = len(coins)
        dp = [0 for i in range(n)]

        for i in range(2, n):
          for left in range(n - i):
            right = left + i
            # i means gap
            # i = 2, left = 0, right = 2
            # i = 2, left = 1, right = 3
            # i = 3, left = 0, right = 3
            # i = 3, left = 1, right = 4 
            for i in range(left + 1, right):
              dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n-1]
    
    def maxCoinsWithMemo(self, nums):
      coins = [1] + nums + [1]
      n = len(coins)
      memo = [[0] * n for _ in range(n)]

      return self.helper(memo, coins, 0, n - 1)
    
    def helper(self, memo, coins, left, right):
      if left + 1 == right:
        return 0
      if memo[left][right] > 0:
        return memo[left][right]
      answer = 0

      for i in range(left + 1, right):
        answer = max(answer, coins[left] * coins[i] * coins[right] 
        + self.helper(memo, coins, left, i) 
        + self.helper(memo, coins, i, right))
      memo[left][right] = answer
      return answer