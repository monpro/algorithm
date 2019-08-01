# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        return self.helper(root, 0, sum)

    def helper(self, root, temp, sum):
        if root is None:
            return
        if root.val + temp == sum and root.left is None and root.right is None:
            return True
        left = self.helper(root.left, temp + root.val, sum)
        right = self.helper(root.right, temp + root.val, sum)
        print(left, right)
        if left or right:
            return True
        else:
            return False
