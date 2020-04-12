# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nodeList = []
        while head:
            nodeList.append(head.val)
            head = head.next
            
        base = 2 ** (len(nodeList) - 1)
        result = 0
        
        for val in nodeList:
            result += base * val
            base //= 2
        
        return result
    def getDecimalValueO1(self, head: ListNode) -> int:
        anotherHead = head
        depth = 0
        while anotherHead:
            depth += 1
            anotherHead = anotherHead.next
        result = 0
        base = 2 ** (depth - 1)
        while head:
            result += base * head.val
            base //= 2
            head = head.next
        
        return result
            

        