# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
      self.maxDepth = 0
      self.val = 0
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root, 1)
        return self.val
    
    def helper(self, node, depth):
      if not node:
        return
      if depth > self.maxDepth:
        self.val = node.val
        self.maxDepth = depth
      self.helper(node.left, depth + 1)
      self.helper(node.right, depth + 1)

        