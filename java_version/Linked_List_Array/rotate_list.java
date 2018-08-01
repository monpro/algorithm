package Linked_List_Array;

import java.util.List;

public class rotate_list {
    int getLength(ListNode head){
        int length = 0;
        while (head != null){
            length += 1;
            head = head.next;
        }
        return length;
    }
    public ListNode rotateRight(ListNode head, int k) {
        // write your code here
        if(head == null){
            return head;
        }

        int rotate_length = k % getLength(head);

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        head = dummy;

        ListNode tail = dummy;
        for(int i = 0 ; i < rotate_length; i++){
            head = head.next;
        }
        while (head.next != null){
            tail = tail.next;
            head = head.next;
        }

        head.next = dummy.next;
        dummy.next = tail.next;
        tail.next = null;
        return dummy.next;




    }
}
