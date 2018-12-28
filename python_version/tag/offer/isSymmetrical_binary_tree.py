from .TreeNode import  TreeNode


class Solution:
    def isSymmetrical(self, pRoot):
        return self.helper(pRoot, pRoot)

    def helper(self, pRoot1, pRoot2):
        if pRoot1 is None and pRoot2 is None:
            return True
        if pRoot1 is None or pRoot2 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False

        return self.helper(pRoot1.left, pRoot2.right) and self.helper(pRoot1.right, pRoot2.left)

