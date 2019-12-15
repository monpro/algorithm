class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
         return 0
        
        n = len(s)
        dps = [0 for _ in range(n)]
        
        for i in range(1, n):
            if s[i] == ')':
                j = i - 1 - dps[i - 1]
                if j >= 0 and s[j] == '(':
                    dps[i] = dps[i - 1] + 2
                    if j - 1 >= 0:
                        dps[i] += dps[j - 1]
        
        return max(dps)