# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
      self.firstElement = None
      self.secondElement = None
      self.prevElement = TreeNode(float('-Inf'))
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        self.firstElement.val, self.secondElement.val = self.secondElement.val, self.firstElement.val

    def traverse(self, root):
      if not root:
        return
      
      self.traverse(root.left)

      if self.firstElement is None and self.prevElement.val >= root.val:
        self.firstElement = self.prevElement
      
      if self.firstElement != None and self.prevElement.val >= root.val:
        self.secondElement = root
      
      self.prevElement = root

      self.traverse(root.right)
      