package arrays;

import java.util.*;

class Solution {
    public int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, (n1, n2) -> (n1[0] == n2[0] ? n1[1] - n2[1]: n2[0] - n1[0]));
        
        List<int[]> result = new ArrayList<>();
        
        for(int[] p: people){
            result.add(p[1], p);
        }
        
        return result.toArray(new int[people.length][2]);
    }
}