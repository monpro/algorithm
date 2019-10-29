class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
          return 0
        if len(nums) == 1:
          return nums[0]
        return max(self.robByRange(nums,0, len(nums) - 2) ,self.robByRange(nums, 1, len(nums) - 1))

    def robByRange(self, nums, start, end):
        if not nums or start > len(nums):
          return 0
        prev, cur = 0, 0
        for i in range(start, end + 1):
          temp = cur
          cur = max(cur, prev + nums[i])
          prev = temp
        return max(cur, prev)

if __name__ == "__main__":
    l = Solution()
    print(l.rob([1,2]))