class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        dummy = ListNode(-1)
        dummy.next = pHead

        cur = pHead
        last = dummy
        while cur is not None and cur.next is not None:
            if cur.val == cur.next.val:
                val = cur.val
                while cur is not None and cur.val == val:
                    cur = cur.next
                last.next = cur
            else:
                last = cur
                cur = cur.next

        return dummy.next

    def reccurision_solution(self,pHead):
        if pHead is None:
            return pHead
        if pHead is not None and pHead.next is None:
            return pHead

        if pHead.next.val == pHead.val:
            current = pHead.next.next
            while current is not None and current.val == pHead.val:
                current = current.next
            return self.reccurision_solution(current)
        else:
            current = pHead.next
            pHead.next = self.reccurision_solution(current)
            return pHead