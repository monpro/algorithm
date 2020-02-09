# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
          return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for i in range(m - 1):
          prev = prev.next
        tail = prev.next
        for i in range(n - m):
          temp = prev.next
          prev.next = tail.next
          tail.next = tail.next.next
          prev.next.next = temp

        return dummy.next