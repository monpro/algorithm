# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []
        stack = []
        result = []
        stack.append(root)
        while stack:
            new_stack = []
            for i in stack:
                if i.left:
                    new_stack.append(i.left)
                if i.right:
                    new_stack.append(i.right)
                result.append(i.val)

            stack = new_stack


        return result

treeNode = TreeNode(1)
treeNode.left = TreeNode(2)
treeNode.right = TreeNode(3)
treeNode.left.left = TreeNode(4)
treeNode.left.right = TreeNode(5)
treeNode.right.left = TreeNode(6)
treeNode.right.right = TreeNode(7)

l = Solution()
print(l.PrintFromTopToBottom(treeNode))

print(treeNode.left.left.val)