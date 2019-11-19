import collections

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
          return []
        k = len(words[0])
        result = []
        for left in range(k):
          d = collections.Counter(words)
          for right in range(left + k, len(s) + 1, k):
            word = s[right - k: right]
            d[word] -= 1
            while d[word] < 0:
              d[s[left: left + k]] += 1
              left += k
            if left + k * len(words) == right:
              result.append(left)
        return result
            
