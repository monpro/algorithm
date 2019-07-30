class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[_ for i in range(len(s2))] for i in range(len(s1))]
        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            if s1[:i] == s3[:i]:
                dp[i][0] = True

        for i in range(1, len(s2) + 1):
            if s2[:i] == s3[:i]:
                dp[0][i] = True

        for i in range(1,len(s1) + 1):
            for j in range(1,len(s2) + 1):
                if s3[i + j - 1] == s1[i - 1]:
                    dp[i][j] |= dp[i - 1][j]
                if s3[i + j - 1] == s2[j - 1]:
                    dp[i][j] |= s2[j - 1]

        return dp[len(s1)][len(s2)]


