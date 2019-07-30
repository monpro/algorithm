class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """

    def findMiddle(self, h):
        slow, fast = h, h.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, h):
        prev = None
        while h:
            tmp = h.next
            h.next = prev
            prev = h
            h = tmp

        return prev

    def reorderList(self, head):
        # write your code here
        if head is None or head.next is None:
            return head

        mid = self.findMiddle(head)
        last = self.reverse(mid.next)
        mid.next = None

        while last:
            tmp = head.next
            head.next = last
            h = last.next
            last.next = tmp
            head = tmp
            last = h



