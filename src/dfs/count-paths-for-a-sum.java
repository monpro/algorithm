package dfs;

import java.util.*;

class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode(int x) {
    val = x;
  }
};

class CountAllPathSum {
  public static int countPaths(TreeNode root, int S) {
    List<Integer> currentPath = new ArrayList<>();

    return dfs(root, S, currentPath);
  }

  public static int dfs(TreeNode root, int S, List<Integer> currentPath){
    if(root == null){
      return 0;
    }

    currentPath.add(root.val);
    int numPath = 0, currentSum = 0;
    for(int i = currentPath.size() - 1; i >= 0; i--){
      currentSum += currentPath.get(i);
      
      if(currentSum == S){
        numPath += 1;
      }
    }

    numPath += dfs(root.left, S, currentPath);
    numPath += dfs(root.right, S, currentPath);

    currentPath.remove(currentPath.size() - 1);
    return numPath;
  }
}