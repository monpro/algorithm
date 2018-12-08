# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        '''
        stack = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next

        result = []
        for i in range(len(stack)):
            val = stack.pop()
            result.append(val)
        '''

        stack = []
        self.helper(listNode, stack)
        return stack

    def helper(self, listNode, stack):
        if listNode:

            if listNode.next:
                self.helper(listNode.next, stack)
            stack.append(listNode.val)
