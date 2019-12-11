# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
          return []
        
        count = {}

        self.helper(root, count)
    
    def helper(self, root, count):
      if not root:
        return 
      if root and not root.left and not root.right:
        val = root.val
        if val in count:
          count[val] += 1
        else:
          count[val] = 1
        return val
      
      else:
        val = root.val + self.helper(root.left, count) + self.helper(root.right, count)

        if val in count:
          count[val] += 1
        else:
          count[val] += 1
