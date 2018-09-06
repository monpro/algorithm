# -*- coding:utf-8 -*-
class Solution:
    global L
    L = []
    def push(self, node):
        L.append(node)
    def pop(self):
        L.pop(-1)
        # write code here
    def top(self):
        return L[0]
        # write code here
    def min(self):
        return min(L)
        # write code here

T = Solution()

T.push(5)
T.push(3)
T.push(4)

print(T.top())
print(T.min())

