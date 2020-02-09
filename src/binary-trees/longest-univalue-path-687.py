# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    result = 0
    def longestUnivaluePath(self, root):
        if not root:
            return 0
        self.helper(root, root.val)
        return self.result
    
    def helper(self, node, val):
        if not node:
            return 0
        
        left = self.helper(node.left, node.val)
        right = self.helper(node.right, node.val)
        self.result = max(self.result, left + right)
        if val == node.val:
            return max(left, right) + 1
        else:
            return 0

        