"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        
        result = 0
        for child in root.children:
            result = max(result, self.maxDepth(child) + 1)
        
        return result
    
    def maxDepthStack(self, root: 'Node') -> int:
        return None
