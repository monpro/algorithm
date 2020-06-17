"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
  def connect(self, root):
    """
        :type root: Node
        :rtype: Node
        """
    if not root:
      return root
    levels = []
    level = []
    queue = [root]
    while len(queue):
      levels.append([i for i in queue])
      for node in queue:
        if node.left:
          level.append(node.left)
        if node.right:
          level.append(node.right)
      queue = level
      level = []

    for level in levels:
      for i in range(len(level) - 1):
        level[i].next = level[i + 1]
      level[-1].next = None
    return root
