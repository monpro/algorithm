# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = float("Inf")
    prev = None
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
          return self.result
        
        self.getMinimumDifference(root.left)
        if self.prev != None:
          self.result = min(self.result, root.val - self.prev)
        
        self.prev = root.val

        self.getMinimumDifference(root.right)

        return self.result