class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # dp[i][j] means whether j could be get from the sum of first i number
        sumVal = sum(nums)
        if sumVal % 2 == 1:
          return False
        sumVal = sumVal // 2
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

    def canPartitionOptiSpace(self, nums):
        sumVal = sum(nums)
        if sumVal % 2 == 1:
          return False
        sumVal = sumVal // 2
        n = len(nums)
        dp = [0 for _ in range(sumVal + 1)]
        dp[0] = 1
        # dp[i] whether you could get sum <= i from the array
        for num in nums:
          for i in range(sumVal, 0, -1):
            if i >= num:
              dp[i] = dp[i] or dp[i - num]
        return dp[sumVal]
          


if __name__ == "__main__":
    l = Solution()
    nums = [1, 2, 5]
    print(l.canPartitionOptiSpace(nums))
        