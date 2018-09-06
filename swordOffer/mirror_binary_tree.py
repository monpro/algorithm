# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        self.reverse(root)

        return root




    def reverse(self,root):
        if root is None:
            return
        elif root.left is None and root.right is None:
            return
        else:
            root.left, root.right = root.right,root.left
            self.reverse(root.left)
            self.reverse(root.right)

