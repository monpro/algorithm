package Linked_List_Array;

public class Partition_list {
    public ListNode partition(ListNode head, int x) {
        // write your code here
        if(head == null){
            return null;
        }
        ListNode leftDummy = new ListNode(0);
        ListNode rightDymmy = new ListNode(0);

        ListNode left = leftDummy, right = rightDymmy;

        while(head != null){
            if(head.val < x){
                left.next = head;
                left = head;
            }
            else{
                right.next = head;
                right = head;
            }
            head = head.next;
        }
        right.next = null;
        left.next = rightDymmy.next;
        return leftDummy.next;
    }
}
