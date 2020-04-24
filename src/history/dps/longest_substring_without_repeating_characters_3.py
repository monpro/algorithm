class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = {}
        left, right = 0, 0
        n = len(s)
        result = 0
        while left < n and right < n:
            if s[right] in visited:
                pos = visited[s[right]]
                left = max(left, pos + 1)
            visited[s[right]] = right
            result = max(result, right - left + 1)
            right += 1
        
        return max(result, right - left)
                
            