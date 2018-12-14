# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) == 0 or len(array[0]) == 0:
            return False
        row, column = 0, len(array[0]) - 1

        while row < len(array) and column >= 0:
            if array[row][column] > target:
                column -= 1

            elif array[row][column] < target:
                row += 1

            elif array[row][column] == target:
                return True

        return False
