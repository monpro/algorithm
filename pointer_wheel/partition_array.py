class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        # write your code here
        left, right = 0, len(nums) - 1
        while left < right:
            while left <= len(nums) - 1 and nums[left] < k:
                left += 1
            if left == len(nums):
                return left

            while right > 0 and nums[right] >= k:
                right -= 1

            if right > left:
                nums[left], nums[right] = nums[right], nums[left]

        return left

