# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        temp = []
        while head:
          temp.append(head.val)
          head = head.next
        base = 1
        result = 0 
        for i in range(len(temp) -1, -1, -1):
          result += base * temp[i]
          base *= 2
        
        return result

    def getDecimalValueBitWise(self, head):
        ans = 0
        while head:
          ans = ans << 1 | head.val
          head = head.next
        return ans
