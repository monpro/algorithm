# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        results = [0 for i in range(number + 1)]
        results[1] = 1
        results[2] = 2

        for i in range(3,number + 1):
            results[i] = results[i - 1] + results[i - 2]

        return results[number]


l = Solution()
print(l.rectCover(0))