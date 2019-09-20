class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(candidates, target, [], result, 0)
        return result
  
    def helper(self, candidates, target, temp, result, index):
      if target == 0:
        result.append([i for i in temp])
        return
      if target < 0 or index >= len(candidates):
        return 
      for i in range(index, len(candidates)):
        temp.append(candidates[i])
        self.helper(candidates, target - candidates[i], temp, result, i)
        temp.pop()
        
if __name__ == "__main__":
    l = Solution()
    print(l.combinationSum([2,3,5], 8))
