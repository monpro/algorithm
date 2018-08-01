package Linked_List_Array;

import bfs.TreeNode;

public class convert_sorted_list_to_binary_search_tree {
    public TreeNode sortedListToBST(ListNode head) {
        // write your code here
        if(head == null){
            return null;
        }
        if(head.next == null){
            return new TreeNode(head.val);
        }
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        //rootNode is the middle
        ListNode rootNode = slow.next;
        slow.next = null;
        TreeNode root = new TreeNode(rootNode.val);
        root.left = sortedListToBST(head);
        root.right = sortedListToBST(rootNode.next);

        return root;


    }
}
