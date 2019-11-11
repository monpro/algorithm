class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
          return 0
        dp = [i for i in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
          j = 0
          while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
        return dp[-1]