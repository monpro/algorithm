# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        result = []
        self.helper(root,expectNumber,[],result)
        return result




    def helper(self,node,extra_number,path,result):
        path.append(node.val)
        if node.left is None and node.right is None:
            if extra_number == node.val:
                result.append(path)
                path = []
            return
        another_path = [i for i in path]
        if node.left:
            self.helper(node.left, extra_number - node.val, path,result)
        if node.right:
            self.helper(node.right,extra_number - node.val, path,result)








l = Solution()
