# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def longestConsecutive(self, root):
        self.longestLength = 0
        self.helper(root)
        return self.longestLength

    def helper(self, root):
        if root is None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)

        temp = 1
        if root.left and root.val + 1 == root.left.val:
            temp = max(temp, left + 1)
        if root.right and root.val + 1 == root.right.val:
            temp = max(temp, right + 1)

        if self.longestLength < temp:
            self.longestLength = temp

        return temp
