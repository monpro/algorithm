class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxLocation = 0
        for i in range(len(nums)):
            if maxLocation < i:
                return False
            if i + nums[i] > maxLocation:
                maxLocation = i + nums[i]
        return True
