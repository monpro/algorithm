class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        last = {char: i for i, char in enumerate(text)}
        stack = []
        for i, char in enumerate(text):
            if char in stack:
                continue
            while stack and stack[-1] > char and i < last[stack[-1]]:
                stack.pop()
            stack.append(char)
        return "".join(stack)
                