# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == 0:
            return 0
        result = [1]
        #find all
        two_queue = [2]
        three_queue = [3]
        five_queue = [5]
        while len(result) < index:
            number = min(three_queue[0],two_queue[0],five_queue[0])
            if two_queue[0] == number:
                two_queue.pop(0)
            if three_queue[0] == number:
                three_queue.pop(0)
            if five_queue[0] == number:
                five_queue.pop(0)
            result.append(number)
            two_queue.append(number * 2)
            three_queue.append(number * 3)
            five_queue.append(number * 5)
        return result[-1]


l = Solution()
l.GetUglyNumber_Solution(20)





