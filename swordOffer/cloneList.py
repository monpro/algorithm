# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        # two hashmap, one to store next, one to store random
        random_map = dict()
        next_map = dict()

        dummy = RandomListNode(-1)
        dummy.next =pHead

        while pHead:
            next_map[pHead] = pHead.next
            pHead = pHead.next

        pHead = dummy.next

        while pHead:
            random_map[pHead] = pHead.random
            pHead = pHead.next

        pHead = dummy.next
        #finish the process of next and random map

        new_head = RandomListNode(pHead.label)
        dummy.next = new_head

        while pHead:
            if next_map[pHead]:
                new_head.next = RandomListNode(next_map[pHead].label)
            if random_map[pHead]:
                new_head.random = RandomListNode(random_map[pHead].label)
            pHead = pHead.next
            new_head = new_head.next

        return dummy.next

