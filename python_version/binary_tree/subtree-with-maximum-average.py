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
    @return: the root of the maximum average of subtree
    """

    def findSubtree2(self, root):
        # write your code here
        if root is None:
            return root

        self.maximum_average = -float("Inf")
        self.result = None

        self.helper(root)

        return self.result

    def helper(self, node):
        if node is None:
            return 0, 0

        left_sum, left_size = self.helper(node.left)
        right_sum, right_size = self.helper(node.right)

        tree_sum, sum_size = node.val + left_sum + right_sum, left_size + right_size + 1

        if tree_sum / sum_size > self.maximum_average:
            self.maximum_average = tree_sum / sum_size
            self.result = node

        return tree_sum, sum_size


