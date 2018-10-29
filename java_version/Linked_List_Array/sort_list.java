package Linked_List_Array;

public class sort_list {
    public ListNode sortList(ListNode head) {
        // write your code here
        quickSort(head,null);
        return head;
    }
    void quickSort(ListNode start, ListNode end){
        if(start == end){
            return;
        }
        ListNode pt = partition(start,end);
        quickSort(start,pt);
        quickSort(pt.next,end);
    }

    ListNode partition(ListNode start, ListNode end){
        int pivotkey = start.val;
        ListNode p1 = start, p2 = start.next;
        while (p2 != end){
            if(p2.val < pivotkey){
                p1 = p1.next;
                swapValue(p1,p2);
            }
            p2 = p2.next;
        }
        swapValue(start,p1);
        return p1;
    }

    void swapValue(ListNode node1, ListNode node2){
        int temp = node1.val;
        node1.val = node2.val;
        node2.val = temp;
    }
}
