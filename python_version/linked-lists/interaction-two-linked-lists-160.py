class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
          return None
        head1 = headA
        head2 = headB
        while head1 != head2:
          if head1 == head2:
            return head1
          if head1:
            head1 = head1.next
          else:
            head1 = headB
          
          if head2:
            head2 = head2.next
          else:
            head2 = headA
        return head1

