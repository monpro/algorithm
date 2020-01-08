class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = 0
        stack = [float('Inf')]
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                result += mid * min(a, stack[-1])
            stack.append(a)
        
        while len(stack) > 2:
            result += stack.pop() * stack[-1]
        
        return result