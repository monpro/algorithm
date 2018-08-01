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

    def inorderTraversal(self, root):
        # write your code here
        result = []
        if root is None:
            return result

        self.helper(root, result)
        return result

    def helper(self, node, result):
        if node is None:
            return
        self.helper(node.left, result)
        result.append(node.val);
        self.helper(node.right, result)
