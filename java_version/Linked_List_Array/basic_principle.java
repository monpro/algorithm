package Linked_List_Array;

import java.util.List;

public class basic_principle {
    void print(ListNode node){
        while (node != null){
            System.out.println(node.val);
            System.out.println("->");
            node = node.next;
        }
    }

    void main(){
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);

        node1.next = node2;
        node2.next = node3;


        ListNode head = node1;
        print(head);

        node1 = node2;
        print(head);
    }
}
