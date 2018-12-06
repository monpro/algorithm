class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    #divide and conquer 分而治之
    def isBalanced(self, root):
        # write your code here
        if root is None:
            return True

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if abs(leftHeight - rightHeight) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, node):
        if node is None:
            return 0

        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)

        return max(leftHeight, rightHeight) + 1