package arrays;

import java.util.Arrays;

class Solution {
    public int findLongestChain(int[][] pairs) {
        if(pairs.length == 0) {
            return 0;
        }
        Arrays.sort(pairs, (n1, n2) -> n1[1] - n2[1]);
        int result = 0;
        int cur = Integer.MIN_VALUE;
        for(int[] pair: pairs) {
            if(cur < pair[0]) {
                cur = pair[1];
                result += 1;
            }
        }
        return result;
        // int left = 0, right = 1;
        // while(left < pairs.length && right < pairs.length) {
        //     int[] pair = pairs[left];
        //     int[] nextPair = pairs[right];
        //     if(pair[1] < nextPair[0]){
        //         result += 1;
        //         left += 1;
        //         right += 1;
        //         if(right == pairs.length) {
        //             result += 1;
        //         }
        //     } else {
        //         right += 1;
        //     }
        // }
        // return result;
    }
}