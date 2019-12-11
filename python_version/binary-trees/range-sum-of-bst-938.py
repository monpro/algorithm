# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = 0
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
          return 
        
        if root.val >= L and root.val <= R:
          self.result += root.val
          self.rangeSumBST(root.left, L, R)
          self.rangeSumBST(root.right, L, R)
        
        if root.val < L:
          self.rangeSumBST(root.right, L, R)
        
        elif root.val >R:
          self.rangeSumBST(root.left, L, R)

        return self.result
          
        