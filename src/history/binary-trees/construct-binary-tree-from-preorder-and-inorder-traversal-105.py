# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
      if len(preorder) == 0 or len(inorder) == 0:
        return None
      rootVal = preorder[0]
      root = TreeNode(preorder[0])
      rootIndex = inorder.index(rootVal)
      leftInorder = inorder[:rootIndex]
      rightInorder = inorder[rootIndex + 1: ]
      leftPreorder = preorder[1: 1 + len(leftInorder)]
      rightPreorder = preorder[1 + len(leftInorder): ]
      root.left = self.buildTree(leftPreorder, leftInorder)
      root.right = self.buildTree(rightPreorder, rightInorder)
      
      return root


if __name__ == "__main__":
  l = Solution()
  print([1,2,3].index(2))
  print([1,2,3][0:1])