# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        assist_stack = []
        while popV:
            if assist_stack and assist_stack[-1] == popV[0]:
                assist_stack.pop()
                popV.pop(0)
            elif pushV and popV and pushV[0] == popV[0]:
                pushV.pop(0)
                popV.pop(0)
            elif pushV:
                assist_stack.append(pushV.pop(0))
            else:
                return False
        return True