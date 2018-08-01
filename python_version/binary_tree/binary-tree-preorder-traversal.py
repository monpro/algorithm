"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        result = []
        if root is None:
            return result

        self.helper(root, result)
        return result

    def helper(self, node, result):
        if node is None:
            return
        result.append(node.val)
        self.helper(node.left, result)
        self.helper(node.right, result)
