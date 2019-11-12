class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4
        dp = [i for i in range(n + 1)]
        dp[0] = 1
        for i in range(5, n + 1):
            dp[i] = max(dp[i - 3] * 3, dp[i])
        #3f - 3 >= 2f - 2 => f >= 5
    
        return dp[-1]
        
        