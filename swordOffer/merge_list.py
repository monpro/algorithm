# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        elif pHead2 is None:
            return pHead1
        else:
            dummy = ListNode(-1)
            head = dummy

            while pHead1 and pHead2:
                if pHead1.val < pHead2.val:
                    head.next = pHead1
                    head = head.next
                    pHead1 = pHead1.next

                else:
                    head.next = pHead2
                    head = head.next
                    pHead2 = pHead2.next


            while pHead1:
                head.next = pHead1
                head = head.next
                pHead1 = pHead1.next

            while pHead2:
                head.next = pHead2
                head = head.next
                pHead2 = pHead2.next

        return dummy.next



