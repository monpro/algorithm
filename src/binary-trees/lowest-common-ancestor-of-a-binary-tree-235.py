# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
          return root
        if root.val < p.val and root.val < q.val:
          return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > q.val and root.val > p.val:
          return self.lowestCommonAncestor(root.left, p, q)
        else:
          return root
    
    def lowestCommonAncestorItera(self, root, p, q):
        if not root:
          return root
        
        node = root
        while node:
          value = node.val
          
          if value < p.val and value < q.val:
            node = node.right
          elif value > p.val and value > q.val:
            node = node.left
          else:
            return node
        return None
