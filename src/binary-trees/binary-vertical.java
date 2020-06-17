import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(final int val) { this.val = val; }
    TreeNode(final int val, final TreeNode left, final TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Node{
    TreeNode treeNode;
    int col;

    public Node(final TreeNode treeNode, final int col){
        this.treeNode = treeNode;
        this.col = col;
    }
}

class Solution {
    
    public List<List<Integer>> verticalOrder(final TreeNode root) {
        final List<List<Integer>> result = new ArrayList<>();
        if(root == null){
            return result;
        }
        
        final Queue<Node> queue = new LinkedList<>();
        final Map<Integer, ArrayList<Integer>> map = new HashMap<>();
        queue.add(new Node(root, 0));
        int minVal = 0, maxVal = 0;
        while(!queue.isEmpty()){
            final Node node = queue.poll();
            final TreeNode treeNode = node.treeNode;
            minVal = Math.min(minVal, node.col);
            maxVal = Math.max(maxVal, node.col);
            if(!map.containsKey(node.col)){
                map.put(node.col, new ArrayList<>());   
            }
            map.get(node.col).add(treeNode.val);
            if(treeNode.left != null){
                queue.add(new Node(treeNode.left, node.col - 1));
            }
            if(treeNode.right != null){
                queue.add(new Node(treeNode.right, node.col + 1));
            }
        }
        
        for(int i = minVal; i <= maxVal; i++){
            result.add(map.get(i));
        }
        
        return result;
        
    }
}