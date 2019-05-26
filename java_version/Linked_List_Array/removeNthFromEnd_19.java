package Linked_List_Array;

public class removeNthFromEnd_19 {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head == null) return null;
        int length = 0;
        int index = 0;
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        head = dummy;
        while (head != null){
            length += 1;
            head = head.next;
        }
        head = dummy;
        ListNode prev = dummy;
        ListNode cur = head;
        while (index <= length - n){
            if(index < length - n) {
                prev = head;
                cur = head.next;
                head = head.next;
                index += 1;
            }
            else {
                prev.next = cur.next;
                cur.next = null;
                break;
            }
        }
        return dummy.next;
    }
}
