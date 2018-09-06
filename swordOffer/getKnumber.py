# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        tinput.sort()
        return tinput[:k]





l = Solution()

print(l.GetLeastNumbers_Solution([4,5,3,2,1],2))