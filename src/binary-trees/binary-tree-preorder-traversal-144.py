# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
          return []
        result = []
        self.helper(root, result)
        return result
    def helper(self, root, result):
      if not root:
        return
      result.append(root.val)
      self.helper(root.left, result)
      self.helper(root.right, result)