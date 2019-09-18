class Solution:
    def titleToNumber(self, s):
      if len(s) == 0:
          return 0
      result = 0
      for i in range(len(s) - 1, -1, -1):
          digit = ord(s[i]) - 65 + 1
          result += 26 ** (len(s) - i - 1) * digit
      return result

if __name__ == "__main__":
    l = Solution()
    l.titleToNumber("A")
        