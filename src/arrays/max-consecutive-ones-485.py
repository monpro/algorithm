class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        count = 0
        result = 0
        for i in nums:
            if i == 0:
                result = max(count, result)
                count = 0
            else:
                count += 1
        result = max(count, result)
        return result