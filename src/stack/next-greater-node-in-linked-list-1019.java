/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int[] nextLargerNodes(ListNode head) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        for(ListNode node = head; node != null; node = node.next){
            arrayList.add(node.val);
        }
        
        int[] result = new int[arrayList.size()];
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < arrayList.size(); i++){
            while(!stack.isEmpty() && arrayList.get(stack.peek()) < arrayList.get(i)){
                result[stack.pop()] = arrayList.get(i);
            }
            stack.add(i);
        }
        return result;
    }
}