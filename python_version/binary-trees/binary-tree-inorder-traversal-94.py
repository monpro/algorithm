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
    @return: Inorder in ArrayList which contains node values.
    inorder--- left, node, right
    """

    def __init__(self):
        self.result = []

    def inorderTraversal(self, root):
        # write your code here
        if root is None:
            return self.result

        self.helper(root)
        return self.result

    def helper(self, node):
        if node is None:
            return
        self.helper(node.left)
        self.result.append(node.val)
        self.helper(node.right)
