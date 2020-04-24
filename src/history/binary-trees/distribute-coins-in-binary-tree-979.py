# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    result = 0
    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            self.result += abs(left) + abs(right)

            return root.val + left + right - 1
        
        dfs(root)
        return self.result

    def distributeCoins(self, root: TreeNode) -> int:
        result = 0
        if not root:
            return 0
        if root.left:
            result += self.distributeCoins(root.left)
            result += abs(root.left.val - 1)
            root.val += root.left.val - 1
        if root.right:
            result += self.distributeCoins(root.right)
            result += abs(root.right.val - 1)
            root.val += root.right.val - 1
        return result
