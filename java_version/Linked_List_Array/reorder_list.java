package Linked_List_Array;

import java.util.List;
import java.util.Map;
import java.util.Stack;

public class reorder_list {
    public void reorderList(ListNode head) {
        // write your code here
        //Given a singly linked list L: L0 → L1 → … → Ln-1 → Ln
        //reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
        //Given 1->2->3->4->null, reorder it to 1->4->2->3->null.
        if(head == null || head.next == null || head.next.next == null){
            return;
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        head = dummy;
        ListNode node = head.next;
        Stack<ListNode> stack = new Stack<>();
        while(node != null){
            stack.push(node);
            node = node.next;
        }
        ListNode start = head;
        int size = stack.size();
        while(stack.size() > Math.ceil((double) size / 2)){
            ListNode end = stack.pop();
            end.next = start.next;
            start.next = end;
            start = start.next.next;
        }
        start.next = null;
    }
}
