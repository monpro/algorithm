
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
 
class Solution {
    public int sumEvenGrandparent(TreeNode root) {
        return helper(root, null, null);
    }
    
    public int helper(TreeNode cur, TreeNode parent, TreeNode grandParent){
        int sum = 0;
        if(cur == null){
            return 0;
        }
        if(grandParent != null && grandParent.val % 2 == 0){
            sum += cur.val;
        }
        
        sum += helper(cur.left, cur, parent);
        sum += helper(cur.right, cur, parent);
        
        return sum;
    }
}