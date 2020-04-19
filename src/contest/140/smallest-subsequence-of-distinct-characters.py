class Solution:
    def smallestSubsequence(self, text: str) -> str:
        lastOccurence = {char: index for index, char in enumerate(text)}
        
        stack = []
        
        for index, char in enumerate(text):
            if char in stack:
                continue
            while len(stack) > 0 and stack[-1] > char and lastOccurence[stack[-1]] > index:
                stack.pop()
            
            stack.append(char)
        return "".join(stack)