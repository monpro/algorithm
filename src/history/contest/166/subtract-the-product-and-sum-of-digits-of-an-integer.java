class Solution {
    public int subtractProductAndSum(int n) {
        int sumDigits = 0;
        int productDigits = 1;
        
        while(n > 0){
            sumDigits += n % 10;
            productDigits *= n % 10;
            n = n / 10;
        }
        
        return productDigits - sumDigits;
    }
}