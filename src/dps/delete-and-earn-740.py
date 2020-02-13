class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        n = max(nums)
        sums = [0 for _ in range(n + 1)]
        
        for num in nums:
            sums[num] += num
        
        for i in range(2, n + 1):
            sums[i] = max(sums[i - 2] + sums[i], sums[i - 1])
            
        
        return sums[n]
    
    