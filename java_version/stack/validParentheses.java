package stack;

import java.util.Stack;

public class validParentheses {
    public boolean isValid(String s) {
        if(s.length() == 0){
            return true;
        }
        Stack<Character> stack = new Stack();
        char[] array = s.toCharArray();
        for(char c: array){
            if(c == '(' || c == '[' || c == '{' ){
                stack.push(c);
            }
            if(stack.isEmpty()){
                return false;
            }
            else if(c == '}'){
                if('{' != stack.pop()){
                    return false;
                }
            }
            else if(c == ']' ){
                if('[' != stack.pop()){
                    return false;
                }
            }
            else if(c == ')'){
                if('(' != stack.pop()){
                    return false;
                }
            }

        }
        return stack.isEmpty();
    }
}
