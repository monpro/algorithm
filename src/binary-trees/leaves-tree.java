/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        helper(result, root);
        return result;
    }
    
    public int helper(List<List<Integer>> result, TreeNode root){
        if(root == null){
            return -1;
        }
        // distance between node and it's furtherest leaf node
        int distance = Math.max(helper(result, root.left), helper(result, root.right)) + 1;
        if(distance == result.size()){
            result.add(new ArrayList<>());
        }
        result.get(distance).add(root.val);
        root.left = root.right = null;
        return distance;
    }
}