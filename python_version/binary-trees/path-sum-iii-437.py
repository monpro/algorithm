
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.pathSumWithNode(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSumWithNode(self, root, sum):
        if not root:
            return 0
        if root.val == sum:
            temp = 1
        else:
            temp = 0
        return temp + self.pathSumWithNode(root.left, sum - root.val) + self.pathSumWithNode(root.right, sum - root.val)


