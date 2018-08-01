"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        if root is None:
            return []
        result = []
        queue = [root]
        while queue != [] :
            mid_result = []
            result.append([i.val for i in queue])
            for i in queue:
                if i.left != '#' and i.left is not None:
                    mid_result.append(i.left)
                if i.right != '#' and i.right is not None:
                    mid_result.append(i.right)
            queue = mid_result
        
        result.reverse()
        return result
        
        
