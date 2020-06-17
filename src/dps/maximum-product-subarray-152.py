class Solution:
    def maxProduct(self, nums):
      result, minNum, maxNUm = nums[0], nums[0], nums[0]
      for i in range(1, len(nums)):
        if nums[i] < 0:
          minNum, maxNUm = maxNUm, minNum
        
        maxNUm = max(nums[i], maxNUm * nums[i])
        minNum = min(nums[i], minNum * nums[i])
        result = max(result, maxNUm)
      return result


        