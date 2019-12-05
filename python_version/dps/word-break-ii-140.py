class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        result = []
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
