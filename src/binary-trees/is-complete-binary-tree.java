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
    /**
    public boolean isCompleteTree(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        while(queue.peek() != null){
            TreeNode node = queue.poll();
            queue.add(node.left);
            queue.add(node.right);
        }
        
        while (!queue.isEmpty() && queue.peek() == null){
            queue.poll();
        }
        return queue.isEmpty();
    }
    **/
    
    public boolean isCompleteTree(TreeNode root) {
        int count = countNodes(root);
        return helper(root, 1, count);
    }
    
    public int countNodes(TreeNode root){
        if(root == null){
            return 0;
        }
        return 1 + countNodes(root.left) + countNodes(root.right);
    }
    
    public boolean helper(TreeNode node, int pos, int total){
        if(node == null){
            return true;
        }
        if(pos > total){
            return false;
        }
        
        return helper(node.left, pos * 2, total) && helper(node.right, pos * 2 + 1, total);
    }
}