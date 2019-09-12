# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
      if not head:
        return None
      if not head.next:
        return TreeNode(head.val)
      slow, fast, prev = head, head, None
      while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
      prev.next = None
      newHead = TreeNode(slow.val)
      newHead.left = self.sortedListToBST(head)
      newHead.right = self.sortedListToBST(slow.next)
      return newHead
        