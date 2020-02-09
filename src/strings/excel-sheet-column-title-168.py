class Solution:
    def convertToTitle(self, n):
      if n == 0:
        return ""
      result = self.helper(n).split('.')
      numberToAlpha = {}
      for i in range(26):
        numberToAlpha[str(i + 1)] = chr(65 + i)
      finalString = ""
      for i in result:
        if len(i) > 0:
          finalString += numberToAlpha[i]
      return finalString

    def helper(self, n):
      if n == 0:
        return ""
      if 1 <= n <= 26:
        return '.' + str(n)
      else:
        if n % 26 !=0:
          return self.helper(n // 26) + self.helper( n % 26)
        else:
          return self.helper(n // 26 - 1) + '.' + '26'

if __name__ == "__main__":
    l = Solution()
    print(26 * 33)
    print(l.convertToTitle(52))
    