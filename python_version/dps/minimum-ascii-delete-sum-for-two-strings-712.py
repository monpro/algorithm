class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        dps = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            dps[i][0] = dps[i - 1][0] + ord(s1[i - 1])
        
        for j in range(1, n + 1):
            dps[0][j] = dps[0][j - 1] + ord(s2[j - 1])
        
        for i in range(1,m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dps[i][j] = dps[i - 1][j - 1]
                else:
                    dps[i][j] = min(dps[i - 1][j] + ord(s1[i - 1]), dps[i][j - 1] + ord(s2[j - 1]))
        
        return dps[m][n]

    def minimumDeleteSumOptimal(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        dps = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1,m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dps[i][j] = dps[i - 1][j - 1] + ord(s[i - 1])
                else:
                    dps[i][j] = max(dps[i - 1][j] , dps[i][j - 1])
        
        return sum(map(ord, s1 + s2)) - 2 * dps[m][n]