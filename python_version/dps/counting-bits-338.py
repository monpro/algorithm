class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        #0 01 10 11 100 101 110 111
        #0 1 1 2 1 2 2 3
        dp = [0 for i in range(num + 1)]
        for i in range(1, num + 1):
          if i & 1 == 0:
            dp[i] = dp[i // 2]
          else:
            dp[i] = dp[i - 1] + 1
        return dp


if __name__ == "__main__":
    l = Solution()
    print(l.countBits(2))
