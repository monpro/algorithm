# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def EntryNodeOfLoop(self, pHead):
        if pHead is None or pHead.next is None:
            return None
        meetNode = self.meetNode(pHead)
        if meetNode is None:
            return None
        length = 1
        next_node = meetNode.next

        while next_node != meetNode:
            length += 1
            next_node = next_node.next
        first_pointer = pHead
        second_pointer = pHead
        for i in range(length):
            first_pointer = first_pointer.next
        while first_pointer != second_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        return first_pointer

    def meetNode(self, pHead):
        slow = pHead
        fast = pHead.next

        while slow:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return slow
            if fast is None:
                return None


'''
test
p = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)
p6 = ListNode(6)


p.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p3

l = Solution()

l.EntryNodeOfLoop(p)

'''