# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    #|left depth - right depth | <= 1
    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True
        if abs(self.maxDepth(pRoot.left) - self.maxDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)







    def maxDepth(self,pRoot):
        if pRoot is None:
            return 0
        return max(self.maxDepth(pRoot.left),self.maxDepth(pRoot.right)) + 1