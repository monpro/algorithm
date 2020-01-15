# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        return self.helper(root, v, d, True)
            
    def helper(self, root, v, d, flag):
        if not root:
            if d == 1:
                return TreeNode(v)
            else:
                return None
        if d == 1:
            newNode = TreeNode(v)
            if flag is True:
                # should be left
                newNode.left = root
                return newNode
            else:
                newNode.right = root
            return newNode
        else:
            root.left = self.helper(root.left, v, d - 1, True)
            root.right = self.helper(root.right, v, d - 1, False)
            return root