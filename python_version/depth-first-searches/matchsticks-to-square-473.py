class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # what's square? 
        # four sides all with same length
        # cannot break the match 
        # fours sides euqal to the longest match
        if len(nums) < 4:
          return False
        temp = [0, 0, 0, 0]
        sumVal = sum(nums)
        if sumVal % 4 != 0:
          return False
        target = sumVal // 4
        nums.sort()
        return self.helper(nums, temp, target, len(nums) - 1)

    def helper(self, nums, temp, target, index):
      if index == -1:
        if temp[0] == target and temp[1] == target and temp[2] == target:
          return True
        else:
          return False
        
      for i in range(4):
        if temp[i] + nums[index] > target:
          continue
        temp[i] += nums[index]
        if self.helper(nums, temp, target, index - 1):
          return True
        temp[i] -= nums[index]
      return False

if __name__ == "__main__":
    l = Solution()
    print(l.makesquare([1,1,2,2,2]))
  