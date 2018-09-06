# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        map = dict()
        for i in numbers:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1

        length = len(numbers)

        for i in numbers:
            if map[i] > length / 2:
                return i

        return 0