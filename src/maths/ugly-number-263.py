class Solution:
    def isUgly(self, num):
      if num == 1:
        return True
      if num == 0:
            return False
      for i in range(2, 6):
        while num % i == 0:
          num /= i
      return num == 1
        
if __name__ == "__main__":
    l = Solution()
    print(l.isUgly(73))
    print(l.isUgly(15))