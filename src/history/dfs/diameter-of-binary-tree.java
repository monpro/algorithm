package history.dfs;

class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode(int x) {
    val = x;
  }
};

class Solution {
    private int result = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return result;
  }

  public int dfs(TreeNode root){
    if(root == null){
      return 0;
    }

    int left = dfs(root.left);
    int right = dfs(root.right);

    result = Math.max(left + right, result);

    return Math.max(left, right) + 1;
  }
}