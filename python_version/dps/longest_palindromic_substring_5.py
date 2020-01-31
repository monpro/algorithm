class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dps = [[0 for _ in range(n)] for _ in range(n)]
        result = ""
        for i in range( n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i < 3 or dps[i + 1][j - 1]:
                        dps[i][j] = 1
                
                if dps[i][j]:
                    if not result or j - i + 1 > len(result):
                        result = s[i: j + 1]
                        
        return result
                        