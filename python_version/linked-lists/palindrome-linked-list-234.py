# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  #do it in O(n) time and O(1) space
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # use the fast and slow pointer trick
        slow, fast = head, head
        revHead = None
        while fast and fast.next:
          fast = fast.next.next
          rev, rev.next, slow = slow, rev, slow.next

        if fast:
          slow = slow.next
        while rev and rev.val == slow.val:
          rev = rev.next
          slow = slow.next
        return not rev
        