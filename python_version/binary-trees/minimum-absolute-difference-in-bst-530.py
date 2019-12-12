# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    inorders = []
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
          return 0
        self.inorder(root)
        result = float('Inf')
        for i in range(1, len(self.inorders)):
          result = min(result, self.inorders[i] - self.inorders[i - 1])
        return result
    def inroder(self, root):
      if not root:
        return 
      self.inroder(root.left)
      self.inorders.append(root.val)
      self.inorder(root.right)
      