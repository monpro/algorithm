# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    prev = None
    max_count = 0
    current_count = 0
    result = []
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dfs(root)
        return self.result
    
    def dfs(self, node):
      if not node:
        return
      self.dfs(node.left)
      if node.val != self.prev:
        self.current_count = 1
      else:
        self.current_count += 1
      
      if self.current_count == self.max_count:
        self.result.append(node.val)
      elif self.current_count > self.max_count:
        self.result = [node.val]
        self.max_count = self.current_count
      
      self.prev = node.val
      self.dfs(node.right)
