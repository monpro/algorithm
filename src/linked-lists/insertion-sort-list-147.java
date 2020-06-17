/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode nodeToInsert, nodePrev= head;
        
        while(head != null && head.next != null){
            if(head.val > head.next.val){
                nodeToInsert = head.next;
                nodePrev = dummy;
                //boundary: first node n.next.val >= nodeToInsert.val
                while(nodePrev.next.val < nodeToInsert.val){
                    nodePrev = nodePrev.next;
                }
                // then we could make an insertion
                head.next = nodeToInsert.next;
                nodeToInsert.next = nodePrev.next;
                nodePrev.next = nodeToInsert;
            }
            else{
                head = head.next;
            }
        }
        
        return dummy.next;
    }
}