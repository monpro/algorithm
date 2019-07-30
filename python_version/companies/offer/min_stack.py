# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.assist = []

    def push(self,node):
        min = self.min()
        if not min or node < self.assist[-1]:
            self.assist.append(node)
        else:
            self.assist.append(min)
        self.stack.append(node)

    def pop(self):
        if self.stack:
            self.assist.pop()
            return self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def min(self):
        if self.assist:
            return self.assist[-1]
