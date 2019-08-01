class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        if len(nums) == 0:
            return 0
        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0
        return nums
