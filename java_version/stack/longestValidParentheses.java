package stack;

import java.util.ArrayList;
import java.util.Stack;

public class longestValidParentheses {
    public int longestValidParentheses(String s) {
        if(s.length() == 0){
            return 0;
        }
        int longest = 0;
        Stack<Integer> stack = new Stack<>();
        char[] array = s.toCharArray();
        for(int i = 0; i < s.length(); i++){
            if(array[i] == '('){
                stack.push(i);
            }
            else {
                if (!stack.isEmpty()) {
                    if (array[stack.pop()] == '(') {
                        stack.pop();
                    } else {
                        stack.push(i);
                    }
                }
                else{
                    stack.push(i);
                }
            }
        }
        if(stack.isEmpty()){
            longest = s.length();
        }
        else{
            int a = s.length();
            int b = 0;
            while (!stack.isEmpty()){
                b = stack.pop();
                stack.pop();
                longest = Math.max(longest, a - b - 1);
                a = b;
            }
            longest = Math.max(longest, a);
        }

        return longest;
    }
    public int longestValidUsingStack(String s){
        Stack<Integer> stack = new Stack<>();
        int result = 0;
        stack.push(-1);
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == ')' && stack.size() > 1 && s.charAt(stack.peek()) == '('){
                stack.pop();
                result = Math.max(result, i - stack.peek());
            }else{
                stack.push(i);
            }
        }
        return result;
    }
}
