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
    @return: Postorder in ArrayList which contains node values.
    """

    def postorderTraversal(self, root):
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
        self.helper(node.right, result)
        result.append(node.val);
