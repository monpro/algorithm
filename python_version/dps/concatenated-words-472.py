class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) == 0:
          return []
        
        result = []
        for word in words:
          if self.helper(word, words):
            result.append(word)
        return result
    
    def helper(self, word, words):
      for i in range(1, len(word)):
        prefix = word[0: i]
        suffix = word[i: ]

        if prefix in words and suffix in words:
          return True
        
        if prefix in words and self.helper(suffix, words):
          return True
        
        if suffix in words and self.helper(prefix, words):
          return True
      return False

if __name__ == "__main__":
    l = Solution()
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    print(l.findAllConcatenatedWordsInADict(words))