# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n<0:
            n = n&0xffffffff
        while n != 0:

            if (n & 1) == 1:
                count += 1
                print(count)
            n = n >> 1

        return count



l = Solution()
print(l.NumberOf1(-1))
