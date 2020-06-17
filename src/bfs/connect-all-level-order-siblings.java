package bfs;

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

class ConnectAllSiblings {
    public static void connect(TreeNode root) {
      if(root == null){
        return;
      }
  
      Queue<TreeNode> queue = new LinkedList<>();
      queue.offer(root);
  
      TreeNode prev = null;
      TreeNode node = null;
      while(!queue.isEmpty()){
        int size = queue.size();
        for(int i = 0; i < size; i++){
          node = queue.poll();
          if(prev == null){
            prev = node;
          }else{
            prev.next = node;
            prev = node;
          }
          if(node.left != null){
            queue.offer(node.left);
          }
          if(node.right != null){
            queue.offer(node.right);
          }
        }
      }
    }
  }