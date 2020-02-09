class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
          return []
        result = []
        self.helper(nums, result, [], 0)
        return result

    def helper(self, nums, result, subset, index):

      if len(subset) >= 2:
        result.append([i for i in subset])
      if index == len(nums):
        return
      used = set()
      for i in range(index, len(nums)):
        if nums[i] in used:
          continue
        if len(subset) == 0 or nums[i] >= subset[-1]:
          used.add(nums[i])
          subset.append(nums[i])
          self.helper(nums, result, subset, i + 1)
          subset.pop()
          

if __name__ == "__main__":
    l = Solution()
    print(l.findSubsequences([4,6,7,7]))
            
      
