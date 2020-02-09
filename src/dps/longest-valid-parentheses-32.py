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
    def longestValidParenthesesUsingStack(self, s):
      if not s:
        return 0
      stack = []
      result = 0
      for i in range(len(s)):
        if s[i] == '(':
          stack.append(i)
        
        else:
          if len(stack) > 0 and s[stack[-1]] == '(':
            curLength = 0
            stack.pop()
            if len(stack) == 0:
              curLength = i + 1
            else:
              curLength = i - stack[-1]
            result = max(result, curLength)
          else:
            stack.append(i)
      return result

if __name__ == "__main__":
    l = Solution()
    print(l.longestValidParenthesesUsingStack("(()"))