"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if root is None:
            return []
        queue = []
        result = []
        queue.append(root)
        while queue:
            mid_result = []
            result.append([i.val for i in queue])
            for e in queue:
                if e.left != '#' and e.left is not None:
                    mid_result.append(e.left)
                if e.right != '#' and e.right is not None:
                    mid_result.append(e.right)
            queue = mid_result
        return result
                
            
