from .TreeNode import TreeNode

class Solution:
    def Mirror(self, root):
        if not root:
            return root
        self.helper(root)

        return root

    def helper(self,root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.helper(root.left)
        self.helper(root.right)
