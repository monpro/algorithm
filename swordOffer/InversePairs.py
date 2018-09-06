# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        if len(data) == 0:
            return 0
        if len(data) == 1:
            return 1
        index = 0
        count = 0
        next_pointer = index + 1
        while index < len(data) - 1:
            while next_pointer <= len(data) - 1:
                if data[next_pointer] < data[index]:
                    count += 1

                next_pointer += 1
            index += 1
            next_pointer  = index + 1
        return count%1000000007

L = Solution()
L.InversePairs([1,2,3,4,5,6,7,0,3])


