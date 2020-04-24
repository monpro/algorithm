class Solution(object):
    def minWindow(self, s, t):
      orderMap = dict()
      for i in s:
        orderMap[i] = 0
      for i in t:
        if i not in orderMap:
          return ''
        else:
          orderMap[i] += 1

      start, end, count, minStart, minLen = 0, 0, len(t), 0, float("Inf")

      while end < len(s):
        if orderMap[s[end]] > 0:
          count -= 1
        orderMap[s[end]] -= 1
        end += 1
        #find the window
        while count == 0:
          if end - start < minLen:
            minStart = start
            minLen = end - start
          
          orderMap[s[start]] += 1
          #try to shrink the window
          if orderMap[s[start]] > 0:
            count += 1
          start += 1

      if minLen != float('Inf'):
        return s[minStart: minStart + minLen]
      else:
        return ''
if __name__ == "__main__":
  l = Solution()
  S = "ADOBECODEBANC"
  T = "ABC"
  print(l.minWindow(S, T))
    