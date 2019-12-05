class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        for i in range(n + 1):
            for word in wordDict:
                if s[i - len(word): i] == word and dp[i - len(word)] == 1 :
                    dp[i] = 1

        return dp[-1]
        



if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    l = Solution()
    print(l.wordBreak(s, wordDict))
