class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return '0'
        
        stack = [num[0]]
        
        for i in range(1, len(num)):
            while len(stack) > 0 and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])
        while k > 0:
            stack.pop()
            k -= 1
        while len(stack) > 0 and  stack[0] == '0':
            stack.pop(0)
        
        return "".join(stack) if len(stack) > 0 else "0"
        