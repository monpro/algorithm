class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s is None and p is None:
            return True
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        #when s = ""
        for i in range(len(p)):
            if p[i] == '*' and dp[0][i - 1]:
                dp[0][i + 1] = True

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == ".":
                    dp[i + 1][j + 1] = dp[i][j]

                elif p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]

                elif p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        #abc
                        #ad*
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]

                    elif p[j - 1] == s[i] or p[j - 1] == ".":
                        #abc
                        #ab#
                        dp[i + 1][j + 1] = dp[i + 1][j - 1] or dp[i][j + 1] or dp[i + 1][j]
        return dp[len(s)][len(p)]