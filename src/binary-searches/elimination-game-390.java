class Solution {
    public int lastRemaining(int n) {
        boolean left = true;
        int remaining = n;
        int step = 1;
        int head = 1;
        
        while(remaining > 1){
            if(left || remaining % 2 == 1){
                head += step;
            }
            remaining /= 2;
            step *= 2;
            left = !left;
        }
        
        return head;
    }
}