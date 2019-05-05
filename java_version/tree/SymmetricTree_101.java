package tree;

import java.util.Stack;

public class SymmetricTree_101 {
    boolean result = true;
    public boolean isSymmetric(TreeNode root) {
        if(root == null){
            return true;
        }
        return helper(root.left, root.right);
    }

    private boolean helper(TreeNode left, TreeNode right){
        if(left == null || right == null){
            return left == right;
        }
        else if(left.val != right.val){
            return false;
        }
        else {
            return helper(left.left, right.right) && helper(left.right, right.left);
        }
    }

    /**
     * using stack to iteratively solve this problem
     * @param root
     * @return
     */
    public boolean isSymmetricWithStack(TreeNode root){
        if(root == null){
            return true;
        }
        Stack<TreeNode> leftStack = new Stack<>();
        Stack<TreeNode> rightStack = new Stack<>();
        leftStack.push(root.left);
        rightStack.push(root.right);

        while (!leftStack.isEmpty()){
            TreeNode left = leftStack.pop();
            TreeNode right = rightStack.pop();
            if(left == null || right == null){
                if(left != right){
                    return false;
                }
            }
            else if(left.val != right.val){
                return false;
            }
            else {
                leftStack.push(left.left);
                rightStack.push(right.right);
                leftStack.push(left.right);
                rightStack.push(right.left);
            }
        }
        return true;
    }
}
