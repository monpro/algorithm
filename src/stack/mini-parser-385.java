/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
class Solution {
    public NestedInteger deserialize(String s) {
        if(s.charAt(0) != '[')
            return new NestedInteger(Integer.valueOf(s));
        Stack<NestedInteger> stack = new Stack<>();
        int start = 1;
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            
            if(ch == '['){
                stack.add(new NestedInteger());
                start = i + 1;
            }
            else if(ch == ','){
                NestedInteger peek = stack.peek();
                if(start< i)
                    peek.add(new NestedInteger(Integer.valueOf(s.substring(start, i))));
                start = i + 1;
            }
            else if(ch == ']'){
                NestedInteger pop = stack.pop();
                if (start < i)
                    pop.add(new NestedInteger(Integer.valueOf(s.substring(start, i))));
                start = i + 1;
                if(!stack.isEmpty())
                    stack.peek().add(pop);
                else
                    return pop;

            }
        }
        return null;
    }
}