class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0, len(nums) - 1

        while left < right - 1:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] < nums[mid - 1]:
                right = mid - 1
            else:
                left = mid + 1


            if nums[left] >= nums[right]:
                return left
            else:
                return right









l = Solution()

print(l.findPeakElement([-2,-1]))



