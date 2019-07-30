

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if head is None or k <= 0:
            return None
        firstPointer = head
        for i in range(k - 1):
            firstPointer = firstPointer.next
            if firstPointer is None:
                return None
        secondPointer = head
        while firstPointer.next:
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next
        return secondPointer


dummy = ListNode(-1)
head = ListNode(1)
dummy.next = head

for i in [2,3,4,5]:
    newNode = ListNode(i)
    head.next = newNode
    head = head.next

l = Solution()
print(l.FindKthToTail(dummy.next,5).val)