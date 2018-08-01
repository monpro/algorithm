class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result,subset =[],[]
        if len(candidates) == 0:
            return result
        candidates = sorted(candidates)
        self.helper(result,subset,candidates,target,0)
        return result

    def helper(self,result,subset,candidates,target,position):
        if target == 0:
            result.append([i for i in subset])
            return
        if candidates[position] > target:
            return
        for i in range(position,len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            subset.append(candidates[i])
            self.helper(result,[i for i in subset],candidates,target - candidates[i],i)
            subset.pop(-1)


