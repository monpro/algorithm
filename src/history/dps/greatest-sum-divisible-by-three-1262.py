class Solution:
    result = 0
    
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dfs(nums, index, temp):
            if (index, temp) in memo:
                return
            if temp % 3 == 0:
                self.result = max(self.result, temp)
                memo[(index, temp)] = 1
            if index == (n):
                return 
            
            for i in range(index, n):
                dfs(nums, i + 1, temp + nums[i])
                dfs(nums, i + 1, temp)
        dfs(nums, 0, 0)
        return self.result
    
    def maxSumDivThreeWithConstantSpace(self, nums: List[int]) -> int:
        s = sum(nums)
        residual = s % 3
        if residual == 0:
            return s
        
        a, b = float('inf'), float('inf')
        res_v = float('inf')
        for num in nums:
            r = num % 3
            if r!= 0:
                if r == residual:
                    res_v = min(num, res_v)
                else:
                    if num < a and  a <=b:
                        b = num
                    elif num < a and a > b:
                        a = num
                    elif num <b and b <=a:
                        a = num
                    elif num <b and b > a:
                        b = num
        max_v = s - min(res_v, a+b)
        return max_v if max_v > 0 else 0