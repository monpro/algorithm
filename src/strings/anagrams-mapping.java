package strings;

import java.util.*;

class Solution {
    public int[] anagramMappings(int[] A, int[] B) {
        // relation[i] = j
        // if A[i] == B[j] -> relation[i] = j
        // HashMap<Integer, Integer> -> <Value, Index> 
        int[] relation = new int[A.length];
        Map<Integer, Integer> indexMap = new HashMap<>();
        for(int i = 0; i < B.length; i++){
            indexMap.put(B[i], i);
        }
        
        for(int i = 0; i < A.length; i++){
            relation[i] = indexMap.get(A[i]);
        }
        
        return relation;
        
    }
}