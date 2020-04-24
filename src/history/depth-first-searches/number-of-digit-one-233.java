class Solution {
    public int countDigitOne(int n) {
        if(n <= 0)
            return 0;
        if(n < 10)
            return 1;
        
        int digits = String.valueOf(n).length();
        
        int base = 1;
        for(int i = 1; i < digits; i++)
            base *= 10;
        
        int firstPosDigit = n / base;
        int remainingDigits = n - base * firstPosDigit;
        
        int result = firstPosDigit * countDigitOne(base - 1);
        
        result += countDigitOne(remainingDigits);
        
        if(firstPosDigit == 1)
            result += n - base + 1;
        else
            result += base;
        
        return result;
    }
}