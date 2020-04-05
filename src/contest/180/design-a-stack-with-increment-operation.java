class CustomStack {
    int n;
    int[] inc;
    Stack<Integer> stack;
    public CustomStack(int maxSize) {
        n = maxSize;
        inc = new int[maxSize];
        stack = new Stack<>();
        
    }
    
    public void push(int x) {
        if(stack.size() < n)
            stack.push(x);
        
    }
    
    public int pop() {
        int i = stack.size() - 1;
        if(i < 0){
            return -1;
        }
        int result = stack.pop() + inc[i];
        inc[i] = 0;
        return result;
        
    }
    
    public void increment(int k, int val) {
        int digit = Math.min(k, stack.size());
        
        for(int i = 0; i < digit; i++){
            inc[i] += val;
        }
        
    }
}