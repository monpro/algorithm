class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        result = 1
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])

        return result

