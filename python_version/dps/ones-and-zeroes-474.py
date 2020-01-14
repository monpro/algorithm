class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        #v dp[m][n] means the the maximum number could be generate from m 0s and n 1s
        dps = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        counterArray = [collections.Counter(val) for val in strs]
        for count in counterArray:
            zeroCount = count['0']
            oneCount = count['1']
            for i in range(m, zeroCount - 1, -1):
                for j in range(n,oneCount - 1, -1):
                    dps[i][j] = max(dps[i - zeroCount][j - oneCount] + 1, dps[i][j])
        
        return dps[-1][-1]
        