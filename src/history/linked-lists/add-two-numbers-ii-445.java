import java.util.Stack;

/**
 * Definition for singly-linked list. public class ListNode { int val; ListNode
 * next; ListNode(int x) { val = x; } }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<ListNode> stackL1 = new Stack<>();
        Stack<ListNode> stackL2 = new Stack<>();
        
        while(l1 != null){
            stackL1.add(l1);
            l1 = l1.next;
        }
        
        while(l2 != null){
            stackL2.add(l2);
            l2 = l2.next;
        }
        
        int carry = 0;
        ListNode dummy = null;
        while(!stackL1.isEmpty() || !stackL2.isEmpty() || carry != 0){
            int v1 = stackL1.size() > 0 ? stackL1.pop().val: 0;
            int v2 = stackL2.size() > 0 ? stackL2.pop().val: 0;
            int sum = v1 + v2 + carry;
            ListNode head = new ListNode(sum % 10);
            head.next = dummy;
            dummy = head;
            
            carry = sum / 10;
            
        }
        
        return dummy;
    }
}