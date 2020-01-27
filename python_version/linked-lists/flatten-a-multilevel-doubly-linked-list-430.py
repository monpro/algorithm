"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack = []
        
        cur = head
        
        while cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                
                cur.next = cur.child
                cur.next.prev = cur
                cur.child = None
            else:
                if cur.next == None and stack:
                    cur.next = stack.pop()
                    cur.next.prev = cur
            
            cur = cur.next
            
        return head
                