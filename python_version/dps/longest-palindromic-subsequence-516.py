class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i] = 1
            preVal = 0
            for j in range(i + 1, n):
                tempVal = dp[j]
                if s[i] == s[j]:
                    dp[j] = preVal + 2
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                preVal = tempVal
        return dp[n - 1]

