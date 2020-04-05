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
    List<TreeNode> inorderList;
    public TreeNode balanceBST(TreeNode root) {
        inorderList = new ArrayList<>();
        inorder(root);
        return build(inorderList, 0, inorderList.size() - 1);
    }
    
    public TreeNode build(List<TreeNode> list, int start, int end){
        if(start > end)
            return null;
        int mid = (start + end) / 2;
        TreeNode root = list.get(mid);
        root.left = build(list, start, mid - 1);
        root.right = build(list, mid + 1, end);
        
        return root;
    }
    
    
    public void inorder(TreeNode root){
        if(root == null)
            return;
        inorder(root.left);
        inorderList.add(root);
        inorder(root.right);

    }
}