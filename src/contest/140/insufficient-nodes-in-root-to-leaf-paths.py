class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if root is None:
            return None
        
        if root.left == root.right == None:
            return None if root.val < limit else root
        
        if root.left:
            root.left = self.sufficientSubset(root.left, limit - root.val)
        
        if root.right:
            root.right = self.sufficientSubset(root.right , limit - root.val)
        
        return root if root.left or root.right else None

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        
        return self.dfs(root, 0, limit)
        
        
    def dfs(self, root, sumVal, limit):
        
        if not root:
            return None
        
        sumVal += root.val
        
        if root.left is None and root.right is None:
            if sumVal < limit:
                return None
            else:
                return root
        
        root.left = self.dfs(root.left, sumVal, limit)
        root.right = self.dfs(root.right, sumVal, limit)
        

        return root if root.left or root.right else None