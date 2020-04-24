class Solution:
    def findDuplicate(self, nums):
      if(len(nums) > 1):
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
          slow = nums[slow]
          fast = nums[nums[fast]]
        fast = 0
        while fast != slow:
          fast = nums[fast]
          slow = nums[slow]
        return slow
      return -1


if __name__ == "__main__":
    l = Solution()
    l.findDuplicate(
[2,5,9,6,9,3,8,9,7,1])
    
        