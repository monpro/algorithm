# -*- coding:utf-8 -*-
class ListNode:
   def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if head is None:
            return
        count = 1
        dummy = ListNode(-1)
        dummy.next = head
        while head.next:
            count += 1
            head = head.next
        if count < k:
            return
        move = count - k
        node = dummy.next
        for i in range(move):
            node = node.next
        return node


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        pre = None

        while pHead:
            next_node = pHead.next
            pHead.next = pre
            pHead = next_node
            pre = pHead

        return pre

