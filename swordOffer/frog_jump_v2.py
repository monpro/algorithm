# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):

        results = [0 for i in range(number + 1)]
        results[0] = 1
        results[1] = 1

        for i in range(2, number + 1):
            for j in range(i):
                results[i] += results[j]

        return results[number]

t = Solution()
print(t.jumpFloorII(10))
