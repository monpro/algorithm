"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        # write your code here
        if root is None:
            return root

        if root.left is None and root.right is None:
            return root

        self.min_number = float("INF")
        self.result = None
        self.helper(root, self.min_number, self.result)

        return self.result

    def helper(self, node, min_number, result):
        if node is None:
            return 0

        left_value = self.helper(node.left, self.min_number, self.result)
        right_value = self.helper(node.right, self.min_number, self.result)

        if left_value + right_value + node.val < self.min_number:
            self.min_number = left_value + right_value + node.val
            self.result = node
        return left_value + right_value + node.val




