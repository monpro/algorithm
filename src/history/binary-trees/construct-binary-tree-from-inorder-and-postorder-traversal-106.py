# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
      if len(postorder) == 0 or len(inorder) == 0:
        return None
      
      root = TreeNode(postorder.pop())
      rootIndex = inorder.index(root.val)
      leftInorder = inorder[:rootIndex]
      rightInorder = inorder[rootIndex + 1: ]
      root.right = self.buildTree(rightInorder, postorder)
      root.left = self.buildTree(leftInorder, postorder)
      return root
