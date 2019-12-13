# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root):
        ans = 0
        level = [(root, 0)]
        while level:
            newLevel = []
            ans = max(ans, level[-1][1] - level[0][1] + 1)
            for node, pos in level:
                if node.left:
                    newLevel.append((node.left, pos * 2))
                if node.right:
                    newLevel.append((node.right, pos * 2 + 1))
            level = newLevel
        return ans


        
        