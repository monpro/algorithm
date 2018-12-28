
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def Merge(self, pHead1, pHead2):
        '''

        :param pHead1:
        :param pHead2:
        :return:
        '''
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        head = None
        cur = None
        while pHead1 and pHead2:
            if head is None:
                if pHead1.val < pHead2.val:
                    head = pHead1
                    cur = pHead1
                    pHead1 = pHead1.next
                else:
                    head = pHead2
                    cur = pHead2
                    pHead2 = pHead2.next

            else:
                if pHead1.val < pHead2.val:
                    cur.next = pHead1
                    pHead1 = pHead1.next
                else:
                    cur.next = pHead2
                    pHead2 = pHead2.next
                cur = cur.next
        if pHead1 is None:
            cur.next = pHead2
        else:
            cur.next = pHead1
        return head


    def Merge_Recurision(self,pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        head = None
        if pHead1.val < pHead2.val:
            head = pHead1
            head.next = self.Merge_Recurision(pHead1.next, pHead2)
        else:
            head = pHead2
            head.next = self.Merge_Recurision(pHead1, pHead2.next)

        return head