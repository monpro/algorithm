class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePaths(self, m, n):
        '''
        :param m:
        :param n:
        :return:
        '''
        prev = [1 for i in range(m)]
        cur = [1 for i in range(m)]
        for i in range(1,n):
            for j in range(1, m):
                cur[j] = prev[j] + cur[j - 1]
                prev = cur
        return cur[m - 1]


if __name__ == "__main__":
    l = Solution()
    print(l.uniquePaths(7,3))