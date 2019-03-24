# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    lastVal = -float("INF")
    firstNode = True

    def isValidBST(self, root):
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        # lastval should < root.val
        if not self.firstNode and self.lastVal >= root.val:
            return False

        self.firstNode = False
        self.lastVal = root.val
        if not self.isValidBST(root.right):
            return False
        return True

    def isValidBSTSimplified(self,root, lessThan = float("inf"),largerThan = float("-inf")):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
            self.isValidBST(root.right, lessThan, max(root.val, largerThan))
