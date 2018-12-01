class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        binary search to determine the mid index
        """
        #mid index is pre element > last element

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            # right part is in order
            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1


            else:
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1






