package dps;

class Solution {
    public int maxProfit(int[] prices) {
        int firstBuy = Integer.MAX_VALUE;
        int firstSell = 0;
        int secondBuy = Integer.MAX_VALUE;
        int secondSell = 0;
        
        for(int p: prices){
            firstBuy = Math.min(p, firstBuy);
            firstSell = Math.max(p - firstBuy, firstSell);
            secondBuy = Math.min(p - firstSell, secondBuy);
            secondSell = Math.max(p - secondBuy, secondSell);
        }
        
        return secondSell;
    }
}