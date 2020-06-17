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

class FindAllTreePaths {
    public static List<List<Integer>> findPaths(TreeNode root, int sum) {
      List<List<Integer>> allPaths = new ArrayList<>();
      List<Integer> current = new ArrayList<>();
  
      dfs(allPaths, current, root, sum);
      return allPaths;
    }
  
    public static void dfs(List<List<Integer>> allPaths, List<Integer> currentPath, TreeNode currentNode, int sum){
      if(currentNode == null){
        return;
      }
      currentPath.add(currentNode.val);
  
      if(currentNode.val == sum && currentNode.left == null && currentNode.right == null){
        allPaths.add(new ArrayList<>(currentPath));
      }else{
        dfs(allPaths, currentPath, currentNode.left, sum - currentNode.val);
        dfs(allPaths, currentPath, currentNode.right, sum - currentNode.val);
      }
  
      currentPath.remove(currentPath.size() - 1);
    }
}