# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
          return True
        left = []
        right = []
        self.getLeaveSequence(root1, left)
        self.getLeaveSequence(root2, right)

        if len(left) != len(right):
          return False
        for i in range(len(left)):
          if left[i] != right[i]:
            return False
        return True

    def getLeaveSequence(self, root, result):
      if not root:
        return 
      if not root.left and not root.right:
        result.append(root.val)
      
      self.getLeaveSequence(root.left, result)
      self.getLeaveSequence(root.right, result)
        