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
    
    def maxProduct(self, root: TreeNode) -> int:
        totals = []

        def getTotals(root):
            if not root:
                return 0
            left = getTotals(root.left)
            right = getTotals(root.right)
            totals.append(left + right + root.val)
            return left + right + root.val
        
        total = getTotals(root)
        result = 0
        for val in totals:
            result = max(result, (total - val) * val)

        return result % (10 ** 9 + 7)
        