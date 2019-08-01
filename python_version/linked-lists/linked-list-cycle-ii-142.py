class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        slow = head
        fast = head
        while slow and fast:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
            return False
