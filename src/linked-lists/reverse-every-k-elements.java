class ListNode {
    int value = 0;
    ListNode next;
  
    ListNode(int value) {
      this.value = value;
    }
  }
  
  class ReverseEveryKElements {
  
    public static ListNode reverse(ListNode head, int k) {
      ListNode cur = head, prev = null, nextNode = null;
      ListNode lastNodePrevPart = null;
      ListNode lastNodeCurPart = null;
      while(true){
        lastNodePrevPart = prev;
        lastNodeCurPart = cur;
        for(int i = 0; cur != null && i < k; i++){
          nextNode = cur.next;
          cur.next = prev;
          prev = cur;
          cur = nextNode;
        }
  
        if(lastNodePrevPart == null){
          head = prev;
        }else{
          lastNodePrevPart.next = prev;
        }
  
        lastNodeCurPart.next = cur;
  
        if(cur == null){
          break;
        }
        prev = lastNodeCurPart;
  
        for(int i = 0; i < k && cur != null; i++){
          prev = cur;
          cur = cur.next;
        }
        if(cur == null){
          break;
        }
      } 
      return head;
    }
}