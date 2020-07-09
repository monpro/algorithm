package arrays;

import java.util.*;

class Solution {
    /**
    public int depthSum(List<NestedInteger> nestedList) {
        if(nestedList == null){
            return 0;
        }
        
        int result = 0;
        int depth = 1;
        
        Queue<NestedInteger> queue = new LinkedList<>(nestedList);
        
        while(!queue.isEmpty()){
            int size = queue.size();
            
            for(int i = 0; i < size; i++){
                NestedInteger element = queue.poll();
                if(element.isInteger()){
                    result += element.getInteger() * depth;
                }else{
                    queue.addAll(element.getList());
                }
            }
            depth += 1;
        }
        
        return result;
    }
    */
    
    public int depthSum(List<NestedInteger> nestedList) {
        return helper(nestedList, 1);
    }
    
    public int helper(List<NestedInteger> nestedList, int depth){
        if(nestedList == null){
            return 0;
        }
        int result = 0;        
        for(NestedInteger element: nestedList){
            if(element.isInteger()){
                result += depth * element.getInteger();
            }else{
                result += helper(element.getList(), depth + 1);
            }
        }
        
        return result;
    }

}