
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
      result = []
      self.helper(root, result, 0)
      return result
    
    def helper(self, root, result,depth):
      if not root:
        return 
      if depth == len(result):
        result.append(result.val)
      self.helper(root.right, result, depth + 1)
      self.helper(root.left, result, depth + 1)

