class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        maxNum, sumVal = max(nums), sum(nums)
        if sumVal % k == 1:
          return False
        
        if maxNum > sumVal // k:
          return False
        visited = [0 for _ in range(len(nums))]
        return self.helper(nums, k, visited, sumVal // k, 0, 0)
    
    def helper(self, nums, k, visited, target, curSum, index):
      if k == 0:
        return True
      
      if curSum == target:
        return self.helper(nums, k - 1, visited, target, 0 , 0)
      
      for i in range(index, len(nums)):
        if not visited[i] and curSum + nums[i] <= target:
          visited[i] = True

          if self.helper(nums, k , visited, target, curSum + nums[i], i + 1):
            return True
          visited[i] = False
      return False
       
      
  
      


