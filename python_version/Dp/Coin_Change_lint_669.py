class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        dp = [0] * (amount + 1)
        for coin in coins:
            if coin < amount:
                dp[coin] = 1
        for i in range(1, amount + 1):
            for coin in coins:
                if dp[i] == 0 and i - coin >= 0 and dp[i - coin] > 0:
                    dp[i] = dp[i - coin] + 1
                elif i - coin >= 0 and dp[i - coin] > 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == 0:
            return -1
        return dp[amount]
