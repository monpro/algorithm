# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # like make the tree in-order traversal
        if not root:
          return root
        leftTail = self.flatten(root.left)
        rightTail = self.flatten(root.right)
        if root.left:
          leftTail.right = root.right
          root.right = root.left
          root.left = None

        if rightTail:
          return rightTail
        if leftTail:
          return leftTail
        return root
