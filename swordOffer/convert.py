
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.arr = []
        for i, j in enumerate(self.arr[:-1]):
            j.next = self.arr[i + 1]
            self.arr[i + 1].left = j
        return self.arr[0]


    def helper(self,node):
        self.helper(node.left)
        self.arr.append(node)
        self.arr.append(node.right)

