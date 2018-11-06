"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []

        result = []
        # to get path
        the_String = "" + str(root.val);
        if root.left is None and root.right is None:
            result.append(the_String)
            return result
        self.helper(root.left, result, the_String)
        self.helper(root.right, result, the_String)
        return result

    def helper(self, node, result, substring):
        if node is None:
            return
        if node.left is None and node.right is None:
            substring += "->"
            substring += str(node.val)
            result.append(substring)
            return

        substring += "->"
        substring += str(node.val)
        new_string = copy.deepcopy(substring)
        self.helper(node.left, result, new_string)
        self.helper(node.right, result, new_string)
