# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        result = []
        for i in array:
            if i % 2 == 1:
                result.append(i)

        for i in array:
            if i % 2 == 0:
                result.append(i)

        return result




l = Solution()

arr = [1,2,3,4,5,6,7]
print(l.reOrderArray(arr))

