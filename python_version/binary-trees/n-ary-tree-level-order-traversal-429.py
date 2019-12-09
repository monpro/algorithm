"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):    
    def levelOrder(self, root):
        # write your code here
        if not root:
            return []
        queue = [root]
        result = []
        while len(queue) > 0:
            n = len(queue)
            temp = []
            for i in range(n):
                node = queue[i]
                temp.append(node)
                if node.children:
                    for child in node.children:
                        queue.append(child)
            result.append(temp)
            queue = [n:]
        return result