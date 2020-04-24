# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
          return root
        # iterative
        queue = [root]
        
        while len(queue) > 0:
          node = queue.pop(0)
          if node.left or node.right:
            node.left, node.right = node.right, node.left
          if node.left:
            queue.append(node.left)
          if node.right:
            queue.append(node.right)
        return root

    def invertTreeRecur(self, root):
      if not root:
        return root
      
      if root.left or root.right:
        root.left, root.right = root.right, root.left
      self.invertTreeRecur(root.left)
      self.invertTreeRecur(root.right)

      
        
            
        