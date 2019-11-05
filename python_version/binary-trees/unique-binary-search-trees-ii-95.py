# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generateSubTrees(1, n)

    def generateSubTrees(self, start, end):
        result = []
        if start > end:
            result.append(None)
            return result
        for i in range(start, end + 1):
            leftSubTrees = self.generateSubTrees(start, i - 1)
            rightSubTrees = self.generateSubTrees(i + 1, end)
        
            for left in leftSubTrees:
                for right in rightSubTrees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    result.append(root)
        return result