class Solution:
    def rotate(self, nums, k) :
        """
        Do not return anything, modify nums in-place instead.
        """''
        if len(nums) <= 1:
            return nums
        k = k % len(nums)
        nums[: len(nums) - k], nums[len(nums) - k:] = nums[len(nums) - k:], nums[:len(nums) - k]
        return nums
    def rotate(self, nums, flag):
        k = k % len(nums)
        self.helper(nums, 0, len(nums) - 1)
        self.helper(0, k - 1)
        self.helper(k, len(nums) - 1)
    def helper(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
if __name__ == "__main__":
  l = Solution()
  print(l.rotate([1,2,3,4,5,6,7],3))