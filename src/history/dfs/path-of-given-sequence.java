package history.dfs;

import java.util.*;

class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode(int x) {
    val = x;
  }
};

class PathWithGivenSequence {
  public static boolean findPath(TreeNode root, int[] sequence) {
    if(root == null){
      return sequence.length == 0;
    }

    return dfs(root, sequence, 0);
  }

  public static boolean dfs(TreeNode root, int[] sequence, int index){
    if(root == null){
      return false;
    }

    if(index >= sequence.length || root.val != sequence[index]){
      return false;
    }

    if(root.left == null && root.right == null && index == sequence.length - 1){
      return true;
    }

    return dfs(root.left, sequence, index + 1) || dfs(root.right, sequence, index + 1);
  }
}