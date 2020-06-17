class Solution {
    public ListNode[] splitListToParts(ListNode root, int k) {
        if(root == null){
            return new ListNode[k];
        }
        ListNode[] result = new ListNode[k];
        int length = 1;
        ListNode node = root;
        while(node.next != null){
            length += 1;
            node = node.next;
        }
        
        int num = length / k;
        int capacity = length % k;
        ListNode cur = root;
        ListNode prev = null;
        for(int i = 0; i < k && cur != null; i++){
            result[i] = cur;
            for(int j = 0; j < num; j++){
                prev = cur;
                cur = cur.next;
            }
            
            if(capacity > 0){
                prev = cur;
                cur = cur.next;
                capacity -= 1;
            }
            prev.next = null;
        }
        return result;
    }
}