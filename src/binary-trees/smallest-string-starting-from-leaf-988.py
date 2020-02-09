# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node, suffix):
            if node is None:
                return suffix
            suffix = chr(ord('a') + node.val) + suffix

            if node.left is None and node.right is None:
              return suffix
            
            elif node.left is None or node.right is None:
              return dfs(node.left, suffix) if node.right is None else dfs(node.right, suffix)
            
            left = dfs(node.left, suffix)
            right = dfs(node.right, suffix)

            return left if left < right else right
        return dfs(root, "")