class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums):
        # write your code here
        # firstly, red -- blue then white--blue

        left, right = 0, len(nums) - 1

        while left < right:
            while left < right and nums[left] == 0:
                left += 1

            while left < right and nums[right] != 0:
                right -= 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        left, right = left, len(nums) - 1

        while left < right:
            while left < right and nums[left] == 1 or nums[left] == 0:
                left += 1

            while left < right and nums[right] == 2:
                right -= 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

