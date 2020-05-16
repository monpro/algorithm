package history.permutation;

import java.util.*;

class Parentheses{
    String s;
    int openCount;
    int closeCount;
    
    public Parentheses(String str, int openCount, int closeCount){
        this.s = str;
        this.openCount = openCount;
        this.closeCount = closeCount;
    }
}

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        
        Queue<Parentheses> queue = new LinkedList<>();
        queue.offer(new Parentheses("", 0, 0));
        
        while(!queue.isEmpty()){
            Parentheses p = queue.poll();
            
            if(p.openCount == n && p.closeCount == n){
                result.add(p.s);
            }else{
                
                if(p.openCount < n){
                    queue.add(new Parentheses(p.s + '(', p.openCount + 1, p.closeCount));
                }
                
                if(p.openCount > p.closeCount){
                    queue.add(new Parentheses(p.s + ')', p.openCount, p.closeCount + 1));
                }
            }
        }
        
        return result;
    }
}