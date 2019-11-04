# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        nodeToInsert = head
        while head and head.next:
          if head.val > head.next.val:
            nodeToInsert = head.next
            nodeToInsertPre = dummy
            while nodeToInsertPre.next.val < nodeToInsert.val:
              nodeToInsertPre = nodeToInsertPre.next
            head.next = nodeToInsert.next
            nodeToInsert.next = nodeToInsertPre.next
            nodeToInsertPre.next = nodeToInsert
          else:
            head = head.next
        return dummy.next

