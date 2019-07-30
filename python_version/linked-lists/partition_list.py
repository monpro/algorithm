"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """

    def partition(self, head, x):
        # write your code here
        if head is None:
            return head
        aHead, bHead = ListNode(0), ListNode(0)
        aTail, bTail = aHead, bHead

        while head is not None:
            if head.val < x:
                aTail.next = head
                aTail = aTail.next

            else:
                bTail.next = head
                bTail = bTail.next

            head = head.next

        bTail.next = None
        aTail.next = bHead.next

        return aHead.next