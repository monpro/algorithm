
class Solution(object):
    def __init__(self):
        self.ans = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        self.pathSumWithNode(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)

        return self.ans

    def pathSumWithNode(self, root, sum):
        if not root:
            return 0
        if root.val == sum:
            self.ans += 1
        self.pathSumWithNode(root.left, sum - root.val)
        self.pathSumWithNode(root.right, sum - root.val)


