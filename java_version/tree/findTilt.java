package tree;

public class findTilt {
    int result = 0;
    public int findTilt(TreeNode root) {
        helper(root);
        return result;

    }

    private int helper(TreeNode root){
        if(root == null){
            return 0;
        }
        int left = helper(root.left);
        int right = helper(root.right);
        result += Math.abs(left - right);
        return left + right + root.val;
    }
}
