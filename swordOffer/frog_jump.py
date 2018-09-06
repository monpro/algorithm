# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):

        results = [0 for i in range(number + 1)]
        results[0] = 1
        results[1] = 1

        for i in range(2,number + 1):
            results[i] = results[i - 1]  + results[i - 2]


        return results[number]


l = Solution()

print(l.jumpFloor(10))
