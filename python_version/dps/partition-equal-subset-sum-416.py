class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # dp[i][j] means whether j could be get from the sum of first i number
        sumVal = sum(nums) // 2
        n = len(nums)
        dp = [[0 for _ in range(sumVal + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
          dp[i][0] = 1

        for i in range(1, n + 1):
          for j in range(sumVal + 1):
            #whether choose current number nums[i - 1]
            dp[i][j] = dp[i - 1][j]
            if j >= nums[i - 1]:
              dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        return dp[n][sumVal]

if __name__ == "__main__":
    l = Solution()
    nums = [1, 5, 11, 5]
    print(l.canPartition(nums))
        