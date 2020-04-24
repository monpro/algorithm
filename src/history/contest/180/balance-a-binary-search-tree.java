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
    public TreeNode balanceBST(TreeNode root) {
        List<TreeNode> inorderList = inorder(root);
        
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
    
    
    public List<TreeNode> inorder(TreeNode root){
        List<TreeNode> result = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        if(root == null)
            return result;
        while(root != null || stack.size() > 0){
            while(root != null){
                stack.push(root);
                root = root.left;
            }
            
            root = stack.pop();
            result.add(root);
            root = root.right;
        }
        return result;
    }
}