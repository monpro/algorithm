class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(k, n, 1, [], result)
        return result
    def helper(self, k, n,digit, temp, result):
      if k < 0:
        return
      if n == 0 and k == 0:
         result.append([i for i in temp])
         return
      for i in range(digit, 10):
        temp.append(i)
        self.helper(k - 1, n - i,i + 1, temp, result )
        temp.pop()

if __name__ == "__main__":
    l = Solution()
    print(l.combinationSum3(3, 9))