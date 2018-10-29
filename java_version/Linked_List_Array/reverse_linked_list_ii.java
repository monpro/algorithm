package Linked_List_Array;

import java.util.List;

public class reverse_linked_list_ii {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        // write your code here
        if(m >= n || head == null){
            return null;
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        head = dummy;
        for(int i =1; i < m;i++){
            head = head.next;
        }
        ListNode preNode = head;
        ListNode mNode = head.next;
        ListNode nNode = mNode;
        ListNode postNode = mNode.next;

        for(int i = m; i < n;i++){
            if(postNode == null){
                return null;
            }
            ListNode temp = postNode.next;
            postNode.next = nNode;
            nNode = postNode;
            postNode = temp;
        }
        mNode.next = postNode;
        preNode.next = nNode;

        return dummy.next;

    }
}
