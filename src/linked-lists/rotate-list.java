class Solution {
    public ListNode rotateRight(ListNode head, int rotations) {
        if(head == null || rotations == 0 || head.next == null){
          return head;
        }
        ListNode lastNode = head;
        int length = 1;
        while(lastNode.next != null){
          length += 1;
          lastNode = lastNode.next;
        }

        int k = rotations % length;
        int lastPartLength = length - k;
        ListNode cur = head;
        for(int i = 0; i < lastPartLength - 1; i++){
          cur = cur.next;
        }
        lastNode.next = head;
        head = cur.next;
        cur.next = null;

        return head;
    }
}