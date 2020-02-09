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
    def lengthOfLISTail(self, nums):
        tails = [0 for i in range(len(nums))]
        size = 0
        for num in nums:
            start ,end = 0, size
            while start != end:
                mid = start + (end - start) // 2
                if tails[mid] < num:
                    start = mid + 1
                else:
                    end = mid
            tails[start] = num
            if start == size:
                size += 1
        return size

                

