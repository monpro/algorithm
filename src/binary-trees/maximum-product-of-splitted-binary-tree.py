class Solution:
    result = 0
    total = 0
    def maxProduct(self, root: TreeNode) -> int:
        
        self.total = self.dfs(root)
        self.dfs(root)
        
        return self.result % (10 ** 9 + 7)
        
    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        self.result = max(self.result, (self.total - left) * left, (self.total - right) * right)
        
        return left + right + root.val
        