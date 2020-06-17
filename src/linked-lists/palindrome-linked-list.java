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
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head, fast = head;

        while(fast != null && fast.next != null){
          slow = slow.next;
          fast = fast.next.next;
        }

        ListNode reverseLastHalf = reverse(slow);
        ListNode lastHead = reverseLastHalf;

        while(reverseLastHalf != null && head != null){
          if(head.val != reverseLastHalf.val){
            break;
          }
          head = head.next;
          reverseLastHalf = reverseLastHalf.next;
        } 

        reverse(lastHead);
        if(head == null || reverseLastHalf == null){
          return true;
        }
        return false;
      }

  public static ListNode reverse(ListNode head){
    ListNode prev = null, temp = null; 
    while(head != null){
      temp = head;
      head = head.next;
      temp.next = prev;
      prev = temp;
    }
    return prev;
  }
}