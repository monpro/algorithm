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
    public int maxLevelSum(TreeNode root) {
        if(root == null){
            return -1;
        }
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int level = 0, result = 0, maxValue = Integer.MIN_VALUE, cur = 0;
        while(queue.size() > 0){
            int size = queue.size();
            level += 1;
            for(int i = 0; i < size; i++){
                TreeNode node = queue.poll();
                cur += node.val;
                if(node.left != null){
                    queue.add(node.left);
                }
                if(node.right != null){
                    queue.add(node.right);
                }
            }
            
            if(maxValue < cur){
                result = level;
                maxValue = cur;
            }
            
            cur = 0;
        }
        
        return result;
        
    }
}