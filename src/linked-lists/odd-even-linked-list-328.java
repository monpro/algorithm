class ListNode {
    int val;
    ListNode next;
    ListNode(final int x) { val = x; }
}

class Solution {
    public ListNode oddEvenList(final ListNode head) {
        if(head == null)
            return head;
        ListNode odd = head, even = head.next;
		final ListNode evenHead = even;
        
        while(even != null && even.next != null){
            odd.next = odd.next.next;
            even.next = even.next.next;
            odd = odd.next;
            even = even.next;
        }
        odd.next = evenHead;
        
        return head;
    }
}