# -*- coding:utf-8 -*-
#double pointer
class Solution:
    def FindContinuousSequence(self, tsum):
        result = []
        low,high = 1, 2
        while high > low:
            cur = (high + low) * (high - low + 1) / 2
            if cur == tsum:
                new_result = []
                for i in range(low, high + 1):
                    new_result.append(i)

                result.append(new_result)
            if cur < tsum:
                high += 1
            else:
                low += 1

        return result


l = Solution()
print(l.FindContinuousSequence(130))
        #use hash dict
