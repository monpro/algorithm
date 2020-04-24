package dps;

class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        if(n == 0 || n == 1)
            return 0;
        int maxProfit = 0;
        for(int i = n - 1; i >= 1; i--){
            if(prices[i] > prices[i - 1]){
                maxProfit += prices[i] - prices[i - 1];
            }
        }
        return maxProfit;
    }
}