class Solution {
    public void reorderList(ListNode head) {
        ListNode slow = head, fast = head;
        while(fast != null && fast.next != null){
          slow = slow.next;
          fast = fast.next.next;
        }
        ListNode reverseLastHalf = reverse(slow);
        ListNode firstHalf = head;
        while(firstHalf != null && reverseLastHalf != null){
          ListNode headTemp = firstHalf.next;
          firstHalf.next = reverseLastHalf;
          firstHalf = headTemp;

          ListNode reverseTemp = reverseLastHalf.next;
          reverseLastHalf.next = firstHalf;
          reverseLastHalf = reverseTemp;
        }
        if(firstHalf != null){
          firstHalf.next = null;
        }
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