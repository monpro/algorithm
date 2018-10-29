package Linked_List_Array;

import java.util.List;

public class revere_nodes_in_k_groups {
    public ListNode reverseKGroup(ListNode head, int k) {
        // write your code here
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        head = dummy;
        while (true){
            head = reverseK(head,k);
            if(head == null){
                break;
            }
        }

        return dummy.next;
    }


    // head -> n1 -> n2 ... nk -> nk+1
    // =>
    // head -> nk -> nk-1 .. n1 -> nk+1
    // return n1
    public ListNode reverseK(ListNode head, int k){
        ListNode nk = head;
        for(int i = 0; i < k; i++){
            if(nk == null){
                return null;
            }
            nk = nk.next;
        }
        if(nk == null){
            return null;
        }
        //reverse
        ListNode n1 = head.next;
        ListNode nkPlus = nk.next;
        ListNode prev = null;
        ListNode curt = n1;

        while (curt != nkPlus){
            ListNode temp = curt.next;
            curt.next = prev;
            prev = curt;
            curt = temp;
        }

        head.next = nk;
        n1.next = nkPlus;

        return n1;

    }
}
