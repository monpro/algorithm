class Solution:
    def reverseWords(self, s):
      if len(s) == 0:
        return s
      s = [ i for i in s.split(' ') if i != " " and i!= ""]
      result = ""
      print(s)
      for i in range(len(s) - 1, -1, -1):
        result += s[i]
        if i != 0:
          result += " "
      return result
        



if __name__ == "__main__":
  test_case_1 = "the sky is blue"
  test_case_2 = "  hello world!  "
  test_case_3 = "a good   example"
  l = Solution()
  print(l.reverseWords("     "))
  # print(l.reverseWords(test_case_1) == "blue is sky the")
  # print(l.reverseWords(test_case_2) == "world! hello")
  # print(l.reverseWords(test_case_3) == "example good a")