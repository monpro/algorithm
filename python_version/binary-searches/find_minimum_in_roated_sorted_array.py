'''
Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

'''


class Solution:
    def findMin(self, nums):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
        start, end = 0, len(nums) - 1
        target = nums[-1]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                start = mid
            else:
                end = mid

        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]
