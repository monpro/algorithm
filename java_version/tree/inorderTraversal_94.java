package tree;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class inorderTraversal_94 {
    List<Integer> result = new ArrayList<>();
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        TreeNode cur = root;
        while (cur != null || !stack.isEmpty()){
            while (cur != null){
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            result.add(cur.val);
            cur = cur.right;
        }

        return result;
        /**
        if(root == null){
            return result;
        }

        helper(root);
        return result;
         **/
    }
    public void helper(TreeNode root){
        if(root == null){
            return;
        }
        helper(root.left);
        result.add(root.val);
        helper(root.right);
    }


}
