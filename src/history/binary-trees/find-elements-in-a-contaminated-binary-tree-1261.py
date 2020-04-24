# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.visited = set()
        self.helper(root, 0)
    
    def helper(self, root, val):
        if root:
            root.val = val
            self.visited.add(val)
            self.helper(root.left, 2 * val + 1)
            self.helper(root.right, 2 * val + 2)
        

    def find(self, target: int) -> bool:
        return target in self.visited
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)