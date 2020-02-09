class Solution:
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2, len(s) + 1):
            single = s[i - 1, i]
            double = s[i - 2, i]
            if '1' < single < '9':
                dp[i] += dp[i - 1]

            if '10' <= double <= "26":
                dp[i] += dp[i - 2]

        return dp[-1]

