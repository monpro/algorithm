package strings;

import java.util.*;

class Solution {
    public String nearestPalindromic(String n) {
        //12345
        int length = n.length();
        int index = length / 2;
        boolean isEven = false;
        
        if(length % 2 == 0){
            index -= 1;
            isEven = true;
        }
        
        long leftNum = Long.parseLong(n.substring(0, index + 1));
        List<Long> candidates = new ArrayList<>();
        // 12321
        candidates.add(getPalindrome(leftNum, isEven));
        // 12421
        candidates.add(getPalindrome(leftNum + 1, isEven));
        // 12221
        candidates.add(getPalindrome(leftNum - 1, isEven));
        // 9999
        candidates.add((long)Math.pow(10, length - 1) - 1);
        // 100001
        candidates.add((long)Math.pow(10, length) + 1);
        
        long diff = Long.MAX_VALUE, result = 0, number = Long.parseLong(n);
        
        for(long candidate: candidates){
            if(candidate == number){
                continue;
            }
            if(Math.abs(candidate - number) < diff){
                diff = Math.abs(candidate - number);
                result = candidate;
            }else if(Math.abs(candidate - number) == diff){
                result = Math.min(result, candidate);
            }
        }
        
        return String.valueOf(result);

    }
    
    
    public Long getPalindrome(long number, boolean isEven){
        long result = number;
        // n -> 12345, number -> 123
        // n -> 123456, number -> 123
        if(!isEven){
            number /= 10;
        }
        
        while(number > 0){
            // 123 -> 1230 + 2
            // 12 -> 1
            result = result * 10 + number % 10;
            number /= 10;
        }
        return result;
    }
}