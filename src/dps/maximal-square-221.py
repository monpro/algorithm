class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
          return 0
        dp = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
        maxVal = 0
        for i in range(1, len(matrix) + 1):
          for j in range(1, len(matrix[0]) + 1):
            if matrix[i - 1][j - 1] == '1':
              dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1  
              maxVal = max(maxVal, dp[i][j])
        return maxVal * maxVal