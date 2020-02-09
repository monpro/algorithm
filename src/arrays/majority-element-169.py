class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority, count = nums[0], 1
        for i in range(1, len(nums)):
          if count == 0:
            majority = nums[i]
            count += 1
          elif majority == nums[i]:
            count += 1
          else:
            count -= 1
        return majority