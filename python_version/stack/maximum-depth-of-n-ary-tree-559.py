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
        stack = [[root, 1]]
        result = 0
        
        while stack:
            node, depth = stack.pop(0)
            if not node:
                continue
            result = max(result, depth)
            for child in node.children:
                stack.append([child, depth + 1])
        return result
