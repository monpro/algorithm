class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        length1 = len(word1)
        length2 = len(word2)
        if length1 == 0:
            return length2
        if length2 == 0:
            return length1
        
        dp = [[0 for i in range(length2 + 1)] for j in range(length1 + 1)]
        for i in range(length1 + 1):
          dp[i][0] = i
        for j in range(length2 + 1):
          dp[0][j] = j
        for i in range(1, length1 + 1):
          for j in range(1, length2 + 1):
            if word1[i - 1] == word2[j - 1]:
              dp[i][j] = dp[i - 1][j - 1]
            else:
              dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[length1][length2]