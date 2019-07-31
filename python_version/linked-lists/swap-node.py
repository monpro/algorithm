
from utils.Node import ListNode


class Solution:
    def swapNodes(self, head, v1, v2):
        dummy = ListNode(0, head)
        cur = dummy
        p1 = None
        p2 = None

        while cur.next is not None:
            if cur.next.val == v1:
                p1 = cur
            if cur.next.val == v2:
                p2 = cur

            cur = cur.next
        if p1 is None or p2 is None:
            return dummy.next

        n1 = p1.next
        n2 = p2.next
        n1_nextnode = n1.next
        n2_nextnode = n2.next

        if p1.next == p2:
            p1.next = n2
            n2.next = n1
            n1.next = n2_nextnode

        elif p2.next == p1:
            p2.next = n1
            n1.next = n2
            n2.next = n1_nextnode

        else:
            p1.next = n2
            n2.next = n1_nextnode
            p2.next = n1
            n1.next = n2_nextnode

        return dummy.next

