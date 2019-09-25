class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        index = 0
        while index < len(nums):
          a = nums[index]
          while index + 1 < len(nums) and nums[index + 1] - nums[index] == 1:
            index += 1
          if a != nums[index]:
            result.append(str(a) + '->' + str(nums[index]))
          else:
            result.append(str(a))
          index += 1
        
        return result
            


if __name__ == "__main__":
    l = Solution()
    print(l.summaryRanges([]))