import collections
class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        counts = collections.defaultdict(int)
        for i in range(len(s) - minSize + 1):
          subString = s[i: i + minSize]
          if len(set(subString)) <= maxLetters:
            counts[subString] += 1
        
        return max(counts.values()) if len(counts) > 0 else 0