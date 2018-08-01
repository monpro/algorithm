"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

import day_3.default_class


class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """

    def mergeTwoLists(self, l1, l2):
        # write your code here

        newHead = ListNode(0)
        dummy = newHead
        while l1 and l2:
            if l1.val < l2.val:
                newHead.next = l1
                l1 = l1.next
            else:
                newHead.next = l2
                l2 = l2.next

            newHead = newHead.next

        while l1:
            newHead.next = l1
            l1 = l1.next
            newHead = newHead.next

        while l2:
            newHead.next = l2
            l2 = l2.next
            newHead = newHead.next

        return dummy.next

