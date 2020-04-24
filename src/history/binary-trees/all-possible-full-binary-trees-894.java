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
    public List<TreeNode> allPossibleFBT(int N) {
        List<TreeNode> result = new ArrayList<>();
        
        if(N == 1){
            result.add(new TreeNode(0));
            return result;
        }
        
        if(N % 2 == 0){
            return result;
        }
        
        for(int l = 1; l < N - 1; l += 2){
            List<TreeNode> left = allPossibleFBT(l);
            List<TreeNode> right = allPossibleFBT(N - l - 1);
            
            for(TreeNode lChild: left){
                for(TreeNode rChild: right){
                    TreeNode root = new TreeNode(0);
                    root.left = lChild;
                    root.right = rChild;
                    result.add(root);
                }
            }
        }
        
        return result;
    }
}