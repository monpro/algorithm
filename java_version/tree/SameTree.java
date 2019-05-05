package tree;

public class SameTree {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null){
            return true;
        }
        else if((p == null && q != null) || (p != null && q == null )){
            return false;
        }
        boolean left = isSameTree(p.left,q.left);
        boolean right = isSameTree(p.right, q.right);
        if(p.val == q.val && left && right){
            return true;
        }else{
            return false;
        }
    }
}
