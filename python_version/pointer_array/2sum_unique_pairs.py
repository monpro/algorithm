class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):
        # write your code here
        count = 0
        nums.sort()
        result = []
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] == target:
                if [nums[left], nums[right]] in result:
                    left += 1
                    right -= 1
                    pass
                else:
                    result.append([nums[left], nums[right]])
                    left += 1
                    right -= 1

        return len(result)