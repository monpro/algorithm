package dfs;

class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode(int x) {
    val = x;
  }
};

class Solution {
    int result = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        // result = Integer.MIN_VALUE;
        dfs(root);
        return result;
    }

  public int dfs(TreeNode root){
    if(root == null){
      return 0;
    }

    int leftValue = dfs(root.left);
    int rightValue = dfs(root.right); 

    leftValue = Math.max(leftValue, 0);
    rightValue = Math.max(rightValue, 0);

    int localMaxValue = root.val + rightValue + leftValue;

    result = Math.max(result, localMaxValue);

    return Math.max(leftValue, rightValue) + root.val;
  }
}