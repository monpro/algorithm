from utils.Node import ListNode


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k == 0:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        fast = dummy
        slow = dummy
        length = 0
        while fast.next:
            length += 1
            fast = fast.next
        k = k % length
        breakPoint = length - k

        for i in range(breakPoint):
            slow = slow.next
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None
        return dummy.next



if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l = Solution()
    newHead = l.rotateRight(l1,7)
    while newHead:
        print(newHead.val, '-')
        newHead = newHead.next