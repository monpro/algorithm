# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        count = collections.defaultdict(list)
        helper(node):
          if not node:
            return "null"
          syntax = "%s, %s, %s".format(str(node.val), str(helper(node.left)), str(helper(node.right)))
          nodes[syntax].append(node)
          return syntax
        
        helper(root)

        return [nodes[syntax][0] for syntax in nodes if len(nodes[syntax]) > 1]
        




        
        