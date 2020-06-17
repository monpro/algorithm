class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        rowLength = len(mat)
        colLength = len(mat[0])
        if rowLength == 0 or colLength == 0:
            return 0
        result = 0
        dp = [[0 for _ in range(colLength + 1)] for _ in range(rowLength + 1)]
        for i in range(1, rowLength + 1):
            for j in range(1, colLength + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]
                left = 1
                right = min(i, j)
                while left <= right:
                    k = left + (right - left) // 2
                    cur = dp[i][j] - dp[i - k][j] - dp[i][j - k] + dp[i - k][j - k]
                    if cur <= threshold:
                        result = max(result, k)
                        left = k + 1
                    else:
                        right = k - 1
        return result
                        