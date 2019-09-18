# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
          return []
        result = []
        queue = [root]
        while len(queue) > 0:
          temp = queue[0].val
          length = len(queue)
          for i in range(length):
            node = queue[i]
            temp = max(node.val, temp)
            if node.left:
              queue.append(node.left)
            if node.right:
              queue.append(node.right)
          result.append(temp)
          queue = queue[length:]
        return result