# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = 0
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 2: if it is covered
        # 1: it is the camera
        # 0: not covered
        def dfs(root):
            if not root:
                return 2
            left, right = dfs(root.left), dfs(root.right)
            if left == 0 or right == 0:
                self.result += 1
                return 1
            if left == 2 and right == 2:
                return 0
            if left == 1 or right == 1:
                return 2
            

        return int(dfs(root) == 0) + self.result