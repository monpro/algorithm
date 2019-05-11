class Solution:
    # O(n) time, quick selection
    def findKthLargest(self, nums, k):
        if len(nums) == 0 or k < 1 or k > len(nums):
            return -1

        return self.partition(nums, 0, len(nums) - 1, len(nums) - k)

    def partition(self, nums, start, end, k):
        """
        During the process, it's guaranteed start <= k <= end
        """
        if start == end:
            return nums[k]

        left, right = start, end
        pivot = nums[start]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        # left is not bigger than right
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)

        return nums[k]