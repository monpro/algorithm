class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] m eans the number of bst built from 1...i
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
          for j in range(i):
            dp[i] += dp[i - j - 1] * dp[j] 
        return dp[n]

if __name__ == "__main__":
    l = Solution()
    print(l.numTrees(3))