# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__():
      self.result = -float('Inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.result
    
    def helper(self, node):
      if not node:
        return 0
      left = max(0, self.helper(node.left))
      right = max(0, self.helper(node,right))
      self.result = max(self.result, left + right + node.val)
      return max(left, right) + node.val

      
        