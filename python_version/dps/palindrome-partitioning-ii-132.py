class Solution:
    def minCut(self, s):
        if len(s) == 0:
            return 0
        n = len(s)
        cut = [0 for _ in range(n)]
        isPal = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            minVal = i
            for j in range(i + 1):
                if s[j] == s[i] and (j + 1 > i - 1 or isPal[i + 1][j - 1]):
                    isPal[j][i] = 1
                    if j == 0:
                        minVal = 0
                    else:
                        minVal = min(minVal, cut[j - 1] + 1)

            cut[i] = minVal
        return cut[n - 1]