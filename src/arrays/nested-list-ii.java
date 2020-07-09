package arrays;

import java.util.*;

class Solution {
    /**
            ---bfs solution---
    public int depthSumInverse(List<NestedInteger> nestedList) {
        if(nestedList == null){
            return 0;
        }
        
        int prev = 0, result = 0;
        Queue<NestedInteger> queue = new LinkedList<>(nestedList);
        
        while(!queue.isEmpty()){
            int size = queue.size();
            int level = 0;
            for(int i = 0; i < size; i++){
                NestedInteger element = queue.poll();
                if(element.isInteger()){
                    level += element.getInteger();
                }else{
                    queue.addAll(element.getList());
                }
            }
            
            prev += level;
            result += prev;
            
            
        }
        return result;
    }
    */
    
    int levelSum = 0;
    int maxDepth = 1;
    
    public int depthSumInverse(List<NestedInteger> nestedList) {
        int depthSum = helper(nestedList, 1);
        // x + 2y + 3z = (x + y + z) *  4 - 3x - 2y - z
        return levelSum * (maxDepth + 1) - depthSum;
    }
    
    public int helper(List<NestedInteger> nestedList, int depth){
        if(nestedList == null){
            return 0;
        }
        
        int result = 0;
        
        for(NestedInteger element: nestedList){
            if(element.isInteger()){
                maxDepth = Math.max(depth, maxDepth);
                levelSum += element.getInteger();
                result += depth * element.getInteger();
            }else{
                result += helper(element.getList(), depth + 1);
            }
        }
        
        
        return result;
    }

}