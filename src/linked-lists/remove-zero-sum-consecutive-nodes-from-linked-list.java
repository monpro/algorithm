/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeZeroSumSublists(ListNode head) {
        ListNode dummy = new ListNode(-1), cur = dummy;
        dummy.next = head;
        int prefix = 0;
        Map<Integer, ListNode> prefixMap = new HashMap<>();
        
        while(cur != null){
            prefix += cur.val;
            
            if(prefixMap.containsKey(prefix)){
                cur = prefixMap.get(prefix).next;
                int newPrefix = prefix + cur.val;
                while(newPrefix != prefix){
                    prefixMap.remove(newPrefix);
                    cur = cur.next;
                    newPrefix += cur.val;
                }
                prefixMap.get(prefix).next = cur.next;
            
            }else{
                prefixMap.put(prefix, cur);
            }
            cur = cur.next;
        }
        return dummy.next;
    }

    public ListNode removeZeroSumSublists(ListNode head) {
        ListNode dummy = new ListNode(0), cur = dummy;
        dummy.next = head;
        int prefix = 0;
        Map<Integer, ListNode> seen = new HashMap<>();
        while(cur != null){
            prefix += cur.val;
            seen.put(prefix, cur);
            cur = cur.next;
        }
        prefix = 0;
        cur = dummy;
        while(cur != null){
            prefix += cur.val;
            cur.next = seen.get(prefix).next;
            cur = cur.next;
        }

        return dummy.next;
    }
}