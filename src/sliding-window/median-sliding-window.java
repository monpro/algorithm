import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        double[] result = new double[nums.length - k + 1];
        DoubleQueue dq = new DoubleQueue();
        for(int i = 0; i < nums.length; i++){
            dq.offer(nums[i]);
            if(i >= k - 1){
                result[i-k+1] = dq.getMedian();
                dq.remove(nums[i - k + 1]);
            }
        }
        return result;
    }
    
    
    class DoubleQueue{
        // lefthalf is a max-heap, to store smaller values
        PriorityQueue<Integer> leftHalf = new PriorityQueue<Integer>(Collections.reverseOrder());
        // righthalf is a min-heal, to store bigger values
        PriorityQueue<Integer> rightHalf = new PriorityQueue<>();
        //the reason to do this, is we can always use leafHalf.peek() and rightHalf.peek() to               fetch the value we want
        
        public void offer(int value){
            leftHalf.offer(value);
            rightHalf.offer(leftHalf.poll());
            
            if(leftHalf.size() < rightHalf.size())
                leftHalf.offer(rightHalf.poll());
        }
        
        public double getMedian(){
            return leftHalf.size() > rightHalf.size() ? leftHalf.peek(): ((double)leftHalf.peek() * 0.5 + rightHalf.peek() * 0.5);
        }
        
        public boolean remove(int value){
            return leftHalf.remove(value) || rightHalf.remove(value);
        }
        
    }
    
}
