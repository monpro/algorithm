# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        return self.helper(root, float('inf'), float('-inf'))

    def helper(self, root, lessThan, largerThan):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.helper(root.left, min(lessThan, root.val), largerThan) and \
            self.helper(root.right, lessThan, max(root.val, largerThan))
