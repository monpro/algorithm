package stack;

class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        
        int[] result = new int[n];
        int pre = 0;
        Stack<Integer> stack = new Stack<>();
        for(String log: logs){
            String[] arr = log.split(":");
            if(arr[1].equals("start")){
                if(!stack.isEmpty())
                    result[stack.peek()] += Integer.valueOf(arr[2]) - pre;
                stack.add(Integer.valueOf(arr[0]));
                pre = Integer.valueOf(arr[2]);
                
            }
            else{
                if(!stack.isEmpty())
                    result[stack.pop()] += Integer.valueOf(arr[2]) - pre + 1;
                pre = Integer.valueOf(arr[2]) + 1;
            }
        }
        
        return result;
    }
}