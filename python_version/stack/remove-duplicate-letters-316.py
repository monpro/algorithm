class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        stack = []
        visited = collections.defaultdict(str)
        for char in s:
            counter[char] -= 1
            if visited[char]:
                continue
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                visited[stack[-1]] = False
                stack.pop()
            stack.append(char)
            visited[char] = True
            
        return ''.join(stack)
        
        