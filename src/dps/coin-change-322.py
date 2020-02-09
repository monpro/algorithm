class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0:
          return -1
        
        dps = [float("Inf") for i in range(amount + 1)]
        dps[0] = 0
        for i in range(1, amount + 1):
          for coin in coins:
            if i - coin >= 0:
              dps[i] = min(dps[i - coin] + 1, dps[i])
        if dps[-1] == float("Inf"):
          return -1
        return dps[-1]

if __name__ == "__main__":
    l = Solution()
    print(l.coinChange([2], 13))