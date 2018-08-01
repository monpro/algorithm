package bfs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class levelOrder {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List result = new ArrayList();
        if(root == null){
            return result;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()){
            int size = queue.size();
            List<Integer> level = new ArrayList<>();
            for(int i = 0; i < size; i++){
                TreeNode node = queue.poll();
                level.add(node.val);
                if(node.left != null){
                    queue.offer(node.left);
                }
                if(node.right != null){
                    queue.offer(node.right);
                }
            }
            result.add(level);
        }
        return result;


    }

    public List<List<Integer>> dfs(TreeNode root) {
        List<List<Integer>> results = new ArrayList<>();
        if(root == null){
            return results;
        }

        int maxLevel = 0;
        while(true){
            List<Integer> level = new ArrayList<>();
            helper(root,level,0,maxLevel);
            if(level.size() == 0){
                break;
            }
            results.add(level);
            maxLevel++;
        }
        return results;
    }

    private void helper(TreeNode root, List<Integer> level,
                        int curtLevel, int maxLevel){
        if(root == null || curtLevel > maxLevel){
            return;
        }
        if(curtLevel == maxLevel){
            level.add(root.val);
            return;
        }

        helper(root.left, level, curtLevel+ 1, maxLevel);
        helper(root.right, level, curtLevel + 1, maxLevel);

    }
}
