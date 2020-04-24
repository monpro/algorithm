class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left, right, result, visited = 0, 0, 0, set()
        
        while left < len(s) and right < len(s):

            if s[right] not in visited:
                visited.add(s[right])
                right += 1
                result = max(result, right - left)
            else:
                visited.remove(s[left])
                left += 1
                
        return result