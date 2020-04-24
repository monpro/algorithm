class Solution:
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
          return []
        hashMap = dict()
        result = []
        for i in range(len(s) - 9):
          subString = s[i: i+10]
          print(subString)
          if subString not in hashMap:
            hashMap[subString] = 1
          else:
            hashMap[subString] += 1
        for key in hashMap:
          if hashMap[key] > 1:
            result.append(key)
        return result





if __name__ == "__main__":
  l = Solution()
  print(l.findRepeatedDnaSequences(""))
  print(l.findRepeatedDnaSequences("AAAAAAAAAAA"))