# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

max_depth = -float("INF")


class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0

        count = max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
        return count

