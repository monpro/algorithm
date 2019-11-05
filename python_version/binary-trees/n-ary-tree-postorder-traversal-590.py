"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
          node = stack.pop()
          result.insert(0, node.val)
          if node.children:
            for i in node.children:
              if i:
                stack.append(i)

        return result