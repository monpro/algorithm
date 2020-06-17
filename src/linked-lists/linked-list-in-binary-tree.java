/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isSubPath(ListNode head, TreeNode root) {
        if(head == null)
            return true;
        if(root == null)
            return false;
        // need to find all paths
        
        return dfs(head, root) || (isSubPath(head, root.left) || isSubPath(head, root.right));
        // if(root.val == head.val){
        //     return isSubPath(head.next, root.left) || isSubPath(head.next, root.right);
        // }else{
        //     return isSubPath(head, root.left) || isSubPath(head, root.right);
        // }
    }
    
    public boolean dfs(ListNode head, TreeNode root){
        if(head == null)
            return true;
        if(root == null)
            return false;
        return (head.val == root.val) && (dfs(head.next, root.left) || dfs(head.next, root.right));
    }
}