class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        result = 0

        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y = y + 1

                result = max(result, y - x)

        return result







