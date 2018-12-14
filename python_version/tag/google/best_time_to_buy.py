class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 数字传递规律 6 -3 + 3 - 5 + 5 - 1 = 6 - 1 = 5
        cur_max, final_max = 0, 0
        for i in range(1, len(prices)):
            cur_max += prices[i] - prices[i - 1]
            cur_max = max(0, cur_max)
            final_max = max(final_max, cur_max)
        return final_max

    '''
    def maxProfit(self, prices):
        if len(prices) == 0:
        return 0
        max_profit = 0
        min_buy = [-1 for i in range(len(prices))]
        min_buy[0] = prices[0]
        for i in range(1,len(prices)):
            profit = prices[i] - min_buy[i - 1]
            if profit > max_profit:
                max_profit = profit
            if prices[i] < min_buy[i - 1]:
                min_buy[i] = prices[i]
            else:
                min_buy[i] = min_buy[i - 1]
        return max_profit

    '''

