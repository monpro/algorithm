class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        valid = collections.defaultdict(int)
        stack = []
        n = len(s)
        for i in range(n):
            char = s[i]
            if char == '(':
                stack.append(i)
            elif char == ')' and len(stack) > 0:
                valid[stack.pop()] = True
                valid[i] = True

                
        res = ""
        for i in range(n):
            if s[i] == ')' or s[i] == '(':
                if valid[i] == True:
                    res += s[i]
            else:
                res += s[i]
        return res
        