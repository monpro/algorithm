# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        if not root:
          return root
        result = []
        return result[k - 1]

    def helper(self, root, result):
      if not root:
        return 
      
      self.helper(root.left, result)
      result.append(root.val)
      self.helper(root.right, result)