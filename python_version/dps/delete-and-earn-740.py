class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        sums = [0 for _ in range(10001)]
        
        for num in nums:
            sums[num] += num
        
        for i in range(2, len(sums)):
            sums[i] = max(sums[i - 2] + sums[i], sums[i - 1])
            
        
        return sums[-1]