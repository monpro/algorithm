# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        prev = None
        cur = pHead
        next_node = cur.next

        while cur:
            next_node = cur.next
            if next_node is None:
                 result = cur
            cur.next = prev
            prev = cur
            cur = next_node

        return result
p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)

p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5

l = Solution()
print(l.ReverseList(p1).next.val)