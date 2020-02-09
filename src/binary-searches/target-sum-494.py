class Solution:
    def findTargetSumWays(self, nums, S):
        if len(nums) == 0:
            return 0
        
        return self.helper(nums,S, 0, 0, {})

    
    def helper(self, nums, S, val, index, memo):
        encoding = str(index) + '->' + str(val)
        if encoding in memo:
            return memo[encoding]
        if index == len(nums):
            if val == S:
                return 1
            else:
                return 0
        num = nums[index]
        left = self.helper(nums, S, val + num, index + 1, memo)
        right = self.helper(nums, S, val - num, index + 1, memo)
        memo[encoding] = left + right
        return left + right
        
    

    # def findTargetSumWaysWithDp(self, nums, S):
    #     sumVal = sum(nums)
    #     if S > sumVal and S < -sumVal:
    #         return 0
    #     dp = [[0 for _ in range(2 * sumVal + 1)] for _ in range(len(nums) + 1)]
