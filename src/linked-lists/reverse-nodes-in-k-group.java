/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode prev = null, cur = head, nextNode = null;
        ListNode lastNodeOfCurList = null;
        ListNode lastNodeOfPrevList = null;
        while(true){
          ListNode node = cur;
          for(int i = 0; node != null && i < k - 1; i++){
              node = node.next;
          }
          if(node == null){
              break;
          }
          lastNodeOfCurList = cur;
          lastNodeOfPrevList = prev;
        
          for(int i = 0; cur != null && i < k; i++){
            nextNode = cur.next;
            cur.next = prev;
            prev = cur;
            cur = nextNode;
          }
          if(lastNodeOfPrevList == null){
            head = prev;
          }else{
            lastNodeOfPrevList.next = prev;
          }

          lastNodeOfCurList.next = cur;

          if(cur == null){
            break;
          }

          prev = lastNodeOfCurList;
        }
        return head;
    }
}