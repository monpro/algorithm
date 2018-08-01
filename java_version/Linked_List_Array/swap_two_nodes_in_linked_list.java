package Linked_List_Array;

import java.util.List;

public class swap_two_nodes_in_linked_list {
    public ListNode swapNodes(ListNode head, int v1, int v2) {
        // write your code here
        if (head == null) {
            return null;
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        head = dummy;

        ListNode v1Prev = null;
        ListNode v2Prev = null;

        while (head.next != null) {
            if (head.next.val == v1) {
                v1Prev = head;
            }
            if (head.next.val == v2) {
                v2Prev = head;
            }
            head = head.next;
        }
        if (v1Prev == null || v2Prev == null) {
            return head;
        }
        ListNode node1 = v1Prev.next;
        ListNode node2 = v2Prev.next;
        ListNode node2Next = node2.next;
        ListNode node1Next = node1.next;
        if(v2Prev.next == v1Prev){
            v2Prev.next = node1;
            node1.next = node2;
            node2.next = node1Next;
        }
        else if(v1Prev.next == v2Prev){
            v1Prev.next = node2;
            node2.next = node1;
            node1.next = node2Next;
        }
        else{
            v1Prev.next = node2;
            node2.next = node1Next;
            v2Prev.next = node1;
            node1.next = node2Next;
        }

        return dummy.next;
    }
}
