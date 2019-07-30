"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    '''

    def find_node(self, head, target):
        prev = None
        while head:
            if head.val == target:
                return [prev, head, head.next]
            else:
                prev = head
                head = head.next

        return None


    def swapNodes(self, head, v1, v2):
        # write your code here
        result_v1 = self.find_node(head,v1)
        result_v2 = self.find_node(head,v2)
        dummy = ListNode(0)
        dummy.next = head
        if result_v1 is None or result_v2 is None:
            return head

        if v1 == v2:
            return head

        prev_v1, head_v1, next_node_v1 = result_v1[0], result_v1[1], result_v1[2]
        prev_v2, head_v2, next_node_v2 = result_v2[0], result_v2[1], result_v2[2]

        if head_v1.next == head_v2 and prev_v1 is not None:
            d = head_v2
            head_v1.next = head_v2.next
            d.next = head_v1

            if prev_v1 is not None:
                prev_v1.next = head_v2
            else:
                pass
        elif head_v2.next == head_v1:
            d = head_v1
            head_v2.next = head_v1.next

            d.next = head_v2
            if prev_v2 is not None:
                prev_v2.next = head_v1
            else:
                pass
            return dummy


        else:
            prev_v1.next = head_v2
            head_v2.next = next_node_v1
            prev_v2.next = head_v1
            head_v1.next = next_node_v2

        return dummy.next
        '''

    def swapNodes(self, head, v1, v2):
        dummy = ListNode(0, head)
        cur = dummy
        p1 = None
        p2 = None

        while cur.next != None:
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

