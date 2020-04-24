class Solution:
    def missingNumber(self, nums):
      result = 0
      for i in range(len(nums) + 1):
        result += i
      return result - sum(nums)

if __name__ == "__main__":
    l = Solution()
    print(l.missingNumber([]))
        