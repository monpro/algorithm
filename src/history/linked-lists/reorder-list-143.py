# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
          return
        
        # find the middle of list
        p1 = head
        p2 = head
        while p2.next and p2.next.next:
          p1 = p1.next
          p2 = p2.next.next
        
        # reverse the half after middle 1 - 2 - 3 - 4 - 5 - 6
        # become 1 - 2 - 3 - 6 - 5 - 4
        preMiddle = p1
        preCur = p1.next
        # preMiddle = 3, preCur = 4
        while preCur.next:
          # cur = 5
          # cur = 6
          cur = preCur.next
          # 4 - 6
          # 4 - None
          preCur.next = cur.next
          # 5 - 4
          # 6 - 5
          cur.next =  preMiddle.next
          # 3 - 6 - 5 - 4
          preMiddle.next = cur
          