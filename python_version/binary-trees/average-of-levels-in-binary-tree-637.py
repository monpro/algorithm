# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        result = []
        mid = []
        queue = [root]
        while queue:
            result.append(sum([node.val for node in queue]) / len(queue))
            for node in queue:
                if node.left:
                    mid.append(node.left)
                elif node.right:
                    mid.append(node.right)
            queue = mid
        return result

        