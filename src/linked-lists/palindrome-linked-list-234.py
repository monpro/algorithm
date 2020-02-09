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
        rev = None
        while fast and fast.next:
          fast = fast.next.next
          rev, rev.next, slow = slow, rev, slow.next

        if fast:
          slow = slow.next
        while rev and rev.val == slow.val:
          rev = rev.next
          slow = slow.next
        return not rev
    def isPalindromeNoSideEffect(self, head):
      rev = None
      fast = head
      while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, head = head, rev, head.next
      
      if fast:
        tail = head.next
      else:
        tail = head
      isPali = True
      while rev:
        if isPali and rev.val == tail.val:
          isPali = True
        else:
          isPali = False
        head, head.next, rev = rev, head, rev.next
        tail = tail.next
      return isPali


        