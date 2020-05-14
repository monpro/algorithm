package history.bfs;

import java.util.*;

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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if(root == null){
          return result;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        TreeNode node = null;
        while(!queue.isEmpty()){
          int size = queue.size();
          for(int i = 0; i < size; i++){
            node = queue.poll();
            if(i == size - 1){
              result.add(node.val);
            }
            if(node.left != null){
              queue.offer(node.left);
            }
            if(node.right != null){
              queue.offer(node.right);
            }
          }
        }
        return result;
    }
}