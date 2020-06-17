import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(final int val) { this.val = val; }
    TreeNode(final int val, final TreeNode left, final TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
class Solution {
    List<Integer> result = new ArrayList<>();
    public List<Integer> boundaryOfBinaryTree(TreeNode root) {
        if(root == null){
            return result;
        }
        
        result.add(root.val);
        getLeftBoundary(root.left);
        getLeaf(root.left);
        getLeaf(root.right);
        getRightBoundary(root.right);
        
        return result;
    }
    
    public void getLeftBoundary(TreeNode node){
        if(node == null || (node.left == null && node.right == null )){
            return;
        }
        result.add(node.val);
        if(node.left != null){
            getLeftBoundary(node.left);
        }else{
            getLeftBoundary(node.right);
        }
    }
    
    public void getLeaf(TreeNode node){
        if(node == null){
            return;
        }
        if(node.left == null && node.right == null){
            result.add(node.val);
            return;
        }
        getLeaf(node.left);
        getLeaf(node.right);
        
    }

    public void getRightBoundary(TreeNode node){
        if(node == null || (node.left == null && node.right == null )){
            return;
        }
        if(node.right != null){
            getRightBoundary(node.right);
        }else{
            getRightBoundary(node.left);
        }
        result.add(node.val);
    }
}