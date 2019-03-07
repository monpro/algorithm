class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        paths = []
        if not root:
            return paths

        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)

        if not left and not right:
            paths.append("" + str(root.val))
            return paths

        for path in left:
            paths.append(str(root.val) + "->" + path)
        for path in right:
            paths.append(str(root.val) + "->" + path)

        return paths