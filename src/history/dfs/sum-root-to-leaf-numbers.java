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
    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
  }

  public static int dfs(TreeNode currentNode, int sum){
    if(currentNode == null){
      return 0;
    }

    sum = 10 * sum + currentNode.val;

    if(currentNode.left == null && currentNode.right == null){
      return sum;
    }
    
    return dfs(currentNode.left, sum) + dfs(currentNode.right, sum); 
  }
}