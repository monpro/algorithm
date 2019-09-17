class Solution:
    def nthUglyNumber(self, n):
        nums = [0 for i in range(n)]
        nums[0] = 1
        index2, index3, index5 = 0, 0, 0
        for i in range(1, len(nums)):
          nums[i] = min(nums[index2] * 2, nums[index3] * 3, nums[index5] * 5)
          if nums[index2] * 2 == nums[i]:
            index2 += 1
          if nums[index3] * 3  == nums[i]:
            index3 += 1
          if nums[index5] * 5 == nums[i]:
            index5 += 1
        return nums[-1]