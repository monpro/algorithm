class Solution:
    def findLength(self, A, B) -> int:
        # dp[i][j] means the longest length of common subarray
        # ending with A[i - 1] and B[j - 1]
        if not A or not B:
            return 0
        result = 0
        dp = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    result = max(result, dp[i][j])
        return result