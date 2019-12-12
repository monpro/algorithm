# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    sumVal = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
          return root
        self.convertBST(root.right)
        root.val += self.sumVal
        self.sumVal = root.val
        self.convertBST(root.left)

        return root
        


        

                
        
