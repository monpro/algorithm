class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 0:
          return ""
        nums = [str(i) for i in nums]
        for i in range(len(nums)):
          for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < nums[j] + nums[i]:
              nums[j], nums[i] = nums[i], nums[j]
        if nums[0] == '0':
          return '0'
        return "".join(nums)

if __name__ == "__main__":
    l = Solution()
    print(l.largestNumber([3,30,34,5,9]))