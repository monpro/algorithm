class Solution:
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        if s[0] == "*":
            dp[1] = 9
        else:
            dp[1] = 1

        for i in range(2, len(s) + 1):
            single = s[i - 1: i]
            double = s[i - 2: i]
            print(single)
            print(double)
            print(double[0], double[1])
            if "1" <= single <= "9":
                dp[i] += dp[i - 1]
            elif single == "*":
                dp[i] += 9 * dp[i - 1]

            if double == "**":
                dp[i] += 26 * dp[i - 2]
            elif double[0] == "*":
                if "0" <= double[1] <= "6":
                    dp[i] += 2 * dp[i - 2]
                elif "7" <= double[1] <= "9":
                    dp[i] += 1 * dp[i - 2]
            elif double[1] == '*':
                if double[0] == '1':
                    dp[i] += 9 * dp[i - 2]
                elif double[0] == '2':
                    dp[i] += 6 * dp[i - 2]
            elif "10" <= double <= "26":
                dp[i] += dp[i - 2]
        return dp[-1]
