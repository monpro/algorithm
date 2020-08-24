package stack;

class Solution {
    /**
    public String parseTernary(String expression) {
        if(expression == null || expression.length() == 0) {
            return "";
        }
        Stack<Character> stack = new Stack<>();
        int n = expression.length() - 1;
        for(int i = n; i >= 0; i--) {
            char ch = expression.charAt(i);
            if(!stack.isEmpty() && stack.peek() == '?') {
                stack.pop();
                char left = stack.pop();
                stack.pop();
                char right = stack.pop();
                if(ch == 'T') {
                    stack.push(left);
                } else {
                    stack.push(right);
                }
            }
            else {
                stack.push(ch);
            }
        }
        return String.valueOf(stack.peek());
    }
    **/
    int index = 0;
    public String parseTernary(String expression) {
        return "" + helper(expression);
    }
    public Character helper(String expression) {
        char ch = expression.charAt(index);
        if(index + 1 == expression.length() || expression.charAt(index + 1) == ':') {
            index += 2;
            return ch;
        }
        index += 2;
        char left = helper(expression), right = helper(expression);
        
        return ch == 'T' ? left: right;
    }
    
    
}