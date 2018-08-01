package bfs;

import java.util.*;

//use bfs level order traverse == > then reverse
public class Binary_Tree_Level_Order_Traversal_II {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null){
            return result;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while(!queue.isEmpty()){
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
            result.add(level);
        }


        int right = result.size() - 1;
        List<List<Integer>> final_result = new ArrayList<>();

        while(right >= 0){
            final_result.add(result.get(right));
            right -= 1;
        }


        return final_result;
    }
}
