# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    result = 0
    def diameterOfBinaryTree(self, root):
        self.helper(root)
        return self.result
        
        
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        self.result = max(self.result, left + right)
        return max(left, right) + 1