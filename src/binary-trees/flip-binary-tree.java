import java.util.*;


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    int index = 0;
    List<Integer> result = new ArrayList<>();
    public List<Integer> flipMatchVoyage(TreeNode root, int[] voyage) {
        return dfs(root, voyage) ? result: Arrays.asList(-1);
    }
    
    public boolean dfs(TreeNode root, int[] voyage) {
        if(root == null) {
            return true;
        }
        if(root.val != voyage[index]) {
            return false;
        }
        index += 1;
        if(root.left != null && root.left.val != voyage[index]) {
            result.add(root.val);
            return dfs(root.right, voyage) && dfs(root.left, voyage);
        }
        return dfs(root.left, voyage) && dfs(root.right, voyage);
        
    }
}
    