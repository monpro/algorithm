class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        Arrays.fill(result, -1);
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < n; i++){
            while(!stack.isEmpty() && nums[stack.peek()] < nums[i]){
                result[stack.pop()] = nums[i];
            }
            stack.push(i);
        }
        for(int i = 0; i < n; i++){
            while(!stack.isEmpty() && nums[stack.peek()] < nums[i]){
                result[stack.pop()] = nums[i];
            }
            stack.push(i);
        }
        return result;
    }

    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        Arrays.fill(result, -1);
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < 2 * n; i++){
            while(!stack.isEmpty() && nums[stack.peek()] < nums[i % n]){
                result[stack.pop()] = nums[i % n];
            }
            stack.push(i % n);
        }
        return result;
    }
}