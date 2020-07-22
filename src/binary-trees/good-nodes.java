class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode next;
  
    TreeNode(int x) {
      val = x;
      left = right = next = null;
    }
  };
  
class Solution {
    int result = 0;
    public int goodNodes(TreeNode root) {
        helper(root, root.val);
        return result;
    }
    
    public void helper(TreeNode root, int maxParentVal){
        if(root == null){
            return;
        }
        if(root.val >= maxParentVal){
            result += 1;
        }
        maxParentVal = Math.max(root.val, maxParentVal);
        helper(root.left, maxParentVal);
        helper(root.right, maxParentVal);
    }
}