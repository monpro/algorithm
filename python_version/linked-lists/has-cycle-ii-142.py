class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        slow, fast = head, head
        isCycle = False
        while slow and fast:
            slow = slow.next
            if fast.next is None:
                return None
            fast = fast.next.next
            if slow == fast:
                isCycle = True
                break

        if not isCycle:
            return None
        while head != fast:
            head = head.next
            fast = fast.next
        return head
