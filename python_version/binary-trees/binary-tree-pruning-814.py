# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if root.val == 0 and not root.left and not root.right:
            return None
        else:
            return root
        