class Node(object):
  def __init__(self, val, left, right, next):
    self.val = val
    self.left = left
    self.right = right
    self.next = next


class Solution(object):
  def connect(self, root):
    """
        :type root: Node
        :rtype: Node
        """
    head = root
    while head:
      nextHead = Node(0)
      nextTail = nextHead
      node = head
      while node:
        if node.left:
          # first time, nextTail = nextHead
          nextTail.next = node.left
          nextTail = node.left
        if node.right:
          nextTail.next = node.right
          nextTail = node.right
        node = node.next
      head = nextHead.next
    return root

