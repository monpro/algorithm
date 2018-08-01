package bfs;

import java.util.*;

public class binary_tree_zigzag_level_order_traversal {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if(root == null){
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        boolean leftToRight = true;
        while (!queue.isEmpty()){
            List<Integer> level = new ArrayList<>();
            int size = queue.size();
            for(int i = 0; i < size; i++){
                TreeNode node = queue.poll();
                if(node.left != null){
                    queue.add(node.left);
                }
                if(node.right != null){
                    queue.add(node.right);
                }
                level.add(node.val);
            }
            if(leftToRight){
                result.add(level);
            }
            else{
                List<Integer> temp = new ArrayList<>();
                int right = level.size();
                while(right >= 0){
                    temp.add(level.get(right));
                    right -= 1;
                }
                result.add(temp);
            }
            leftToRight = !leftToRight;

        }
    return result;
    }
}
