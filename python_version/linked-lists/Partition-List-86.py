from utils.Node import ListNode


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
        leftHead, rightHead = ListNode(-1), ListNode(-1)
        leftTail, rightTail = leftHead, rightHead
        while head is not None:
            if head.val < x:
                leftTail.next = head
                leftTail = leftTail.next
            else:
                rightTail.next = head
                rightTail = rightTail.next
            head = head.next
        rightTail.next = None
        leftTail.next = rightHead.next

        return leftHead.next
