class Solution:
    def findMin(self, nums):
        return self.helper(nums,0, len(nums) - 1)

    def helper(self,nums,left,right):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]

        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid
            else:
                if left + 1 == right:
                    return min(nums[left], nums[right])
                else:
                    left_min = self.helper(nums,left, mid)
                    right_min = self.helper(nums, mid + 1, right)
                    return min(left_min, right_min)
        return min(nums[left], nums[right])
