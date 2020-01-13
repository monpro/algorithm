class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack, preorder = [], preorder.split(',')
        for value in preorder:
            while stack and value == stack[-1] == '#':
                stack.pop()
                if not stack:
                    return False
                stack.pop()
            stack.append(value)
        return stack == ['#']