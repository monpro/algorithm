# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, False)
    
    def helper(self, node, isLeft):
      if not node:
        return 0
      
      if not node.left and not node.right and isLeft:
        return node.val
      
      return self.helper(node.left, True) + self.helper(node.right, False)
