class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for(int i: nums){
            queue.offer(i);
            if(queue.size()  > k)
                queue.poll();
        }
        
        return queue.poll();
    }
}