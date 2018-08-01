# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''

public class Solution {
    public int longestConsecutive(TreeNode root) {
        return (root==null)?0:Math.max(dfs(root.left, 1, root.val), dfs(root.right, 1, root.val));
    }



    public int dfs(TreeNode root, int count, int val){
        if(root==null) return count;
        count = (root.val - val == 1)?count+1:1;
        int left = dfs(root.left, count, root.val);
        int right = dfs(root.right, count, root.val);
        return Math.max(Math.max(left, right), count);
    }
}
'''

class Solution(object):
    def longestConsecutive(self, root):

        if root is None:
            return 0

        return max(self.dfs(root.left,1,root.val), self.dfs(root.right,1,root.val))

    def dfs(self,root,count,val):
        if root is None:
            return count
        if root.val - val == 1:
            count += 1
        else:
            count = 1
        left = self.dfs(root.left, count,root.val)
        right = self.dfs(root.right, count,root.val)
        return max(max(left,right),count)


        """
        :type root: TreeNode
        :rtype: int
        """

