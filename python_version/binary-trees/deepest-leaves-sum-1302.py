# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    max_depth = 0
    result = 0
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        self.dfs(root, 1)
        return self.result
    
    def dfs(self, root, depth):
        if root is None:
            return
        if depth > self.max_depth:
            self.max_depth = depth;
            self.result = 0
            
        if depth == self.max_depth:
            self.result += root.val
            
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)