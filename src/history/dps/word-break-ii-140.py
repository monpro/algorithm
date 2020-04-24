class Solution(object):
    def wordBreakWithMemo(self, s, wordDict):
      return self.helperWithMemo(s, wordDict, {})
    
    def helperWithMemo(self, s, wordDict, memo):
      if s in memo:
        return memo[s]
      if not s:
        return []

      result = []
      for word in wordDict:
        if s.startswith(word):
          if len(word) == len(s):
            result.append(word)
          else:
            rightResults = self.helperWithMemo(s[len(word): ], wordDict, memo)
            for item in rightResults:
              result.append(word + " " + item)
      memo[s] = result
      return result    




    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        result = []
        memo = {}
        self.helper(s, wordDict, result, [], 0)
        return result
    
    def helper(self, s, wordDict, result, temp, index):
      if index == len(s):
        result.append(" ".join(temp))
        return
      
      for i in range(index, len(s) + 1):
        for word in wordDict:
          if s[index: i] == word:
            temp.append(word)

            self.helper(s, wordDict, result, temp, i)
            temp.pop()
      

if __name__ == "__main__":
    l = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]

    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]

    print(l.wordBreak(s, wordDict))
