class Solution(object):

    def finalSolution(self, words):
      result = []
      word_dict = set(words)
      for word in words:
        word_dict.remove(word)
        if self.check(word, word_dict) is True:
          result.append(word)
        word_dict.add(word)
      return result

    def check(self, word, word_dict):
      if word in word_dict:
        return True
      
      for i in range(len(word), 0, -1):
        if word[: i] in word_dict and self.check(word[i: ], word_dict):
          return True
      return False
      
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) == 0:
          return []
        
        result = []
        for word in words:
          if self.helper(word, words, {}):
            result.append(word)
        return result
    
    def helper(self, word, words, memo):
      if memo[word]:
        return memo[word]
      for i in range(1, len(word)):
        prefix = word[0: i]
        suffix = word[i: ]

        if prefix in words and suffix in words:
          memo[word] = True
          return True
        
        if prefix in words and self.helper(suffix, words):
          memo[word] = True
          return True
        
        if suffix in words and self.helper(prefix, words):
          memo[word] = True
          return True
      return False

if __name__ == "__main__":
    l = Solution()
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    print(l.findAllConcatenatedWordsInADict(words))