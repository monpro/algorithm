package stack;


class Pair{
    int min, max;
    public Pair(int min, int max){
        this.min = min;
        this.max = max;
    }
}


class Solution {
    public boolean find132pattern(int[] nums) {
        Stack<Pair> stack = new Stack<>();
        
        for(int n: nums){
            if(stack.isEmpty() || stack.peek().min > n){
                stack.push(new Pair(n, n));
            }
            else if(stack.peek().min < n ){
                Pair last = stack.pop();
                if(n < last.max) 
                    return true;
                else{
                    last.max = n;
                    while(!stack.isEmpty() && n >= stack.peek().max)
                        stack.pop();
                    
                    if(!stack.isEmpty() && stack.peek().min < n)
                        return true;
                    stack.push(last);
                }
            }
        }
        return false;
    }
}