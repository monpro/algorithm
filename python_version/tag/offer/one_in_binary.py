# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1_solution_a(self, n):
        count = 0
        while n:
            if n & 1:
                count += 1
                n = n >> 1

        return count

    def Numberof1_solution_b(self,n):
        count = 0
        flag = 1
        while flag:
            if n & flag:
                count += 1
            flag = flag << 1
            print(count)
        return count

    def Numberof1_ultimate(self,n):
        count = 0
        while n:
            count += 1
            n = (n - 1) & n
            print(n)

        return count



