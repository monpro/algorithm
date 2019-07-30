class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, nums, target):
        # write your code here
        left, right = 0, len(nums) - 1

        while left < right:

            if nums[left] + nums[right] < target:
                left += 1

            elif nums[left] + nums[right] > target:
                right -= 1


            elif nums[left] + nums[right] == target:
                return [left + 1, right + 1]

        return []

    def twoSum_less_than_equal_to(self, nums, target):
        # write your code here
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] <= target:
                count += right - left
                left += 1

            else:
                right -= 1

        return count

    def twoSum_greater(self, nums, target):
        # write your code here
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                count += right - left

                right -= 1
            else:
                left += 1

        return count
    def twoSumClosest(self, nums, target):
        # write your code here
        # first_closest, second_closest
        # while there is a problem
        import math as math
        nums.sort()

        left, right = 0, len(nums) - 1

        diff = float('Inf')

        while left < right:
            if nums[left] + nums[right] == target:
                return 0

            elif nums[left] + nums[right] > target:
                diff = min(diff, math.fabs(nums[left] + nums[right] - target))
                right -= 1

            else:
                diff = min(diff, math.fabs(nums[left] + nums[right] - target))
                left += 1

        return int(diff)
