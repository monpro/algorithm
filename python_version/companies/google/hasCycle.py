class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        hashSet = set()
        hashSet.add(head)
        while head.next:
            if head.next in hashSet:
                return True
            else:
                hashSet.add(head)
                head = head.next
        return False