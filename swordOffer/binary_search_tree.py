# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        flag = True
        if pRoot is None:
            return False
        print(self.helper(pRoot.left))
        print(self.helper(pRoot.right))
        result = self.helper(pRoot.left) and self.helper(pRoot.right)
        return result


    def helper(self,pRoot):
        if pRoot.left is None and pRoot.right is None:
            return True
        if pRoot.left is None and pRoot.right.val <= pRoot.val:
            return False
        if pRoot.right is None and pRoot.left.val >= pRoot.val:
            return False
        if pRoot.left.val >= pRoot.val or pRoot.right.val <= pRoot.val:
            return False

        self.helper(pRoot.left)
        self.helper(pRoot.right)
        return True

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

l = Solution()
print(l.IsBalanced_Solution(root))