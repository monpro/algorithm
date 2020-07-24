
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
    public int largestBSTSubtree(TreeNode root) {
        int[] res = largestBst(root);
        return res[2];
    }
    
    public int[] largestBst(TreeNode root){
        if(root == null){
            return new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE, 0};
        }
        int[] left = largestBst(root.left);
        int[] right = largestBst(root.right);
        if(root.val > left[1] && root.val < right[0]){
            return new int[]{Math.min(root.val, left[0]), Math.max(root.val, right[1]), 1 + left[2] + right[2]};
        }else{
            return new int[]{Integer.MIN_VALUE, Integer.MAX_VALUE, Math.max(left[2], right[2])};
        }
    }
}