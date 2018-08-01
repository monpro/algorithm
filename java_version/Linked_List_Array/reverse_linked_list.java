package Linked_List_Array;

public class reverse_linked_list {
    public ListNode reverse(ListNode head) {
        // write your code here
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        head = dummy;

        ListNode prev = null;
        ListNode curt = head.next;

        while(curt != null){
            ListNode temp = curt.next;
            curt.next = prev;
            prev = curt;
            curt = temp;
        }
        dummy.next = prev;
        return dummy.next;
    }
}
