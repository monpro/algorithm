# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        #relative condition should remain the same
        map = dict()
        #only a reverse
        for i in range(len(pushV)):
            map[pushV[i]] = i
        if set(pushV) != set(popV):
            return False


        j = 0
        flag = False
        while j + 1 < len(popV):
            if flag:
                while j + 1 < len(popV):
                    if map[popV[j]] > map[popV[j + 1]]:
                        j += 1
                    else:
                        return False
                break

            if map[popV[j]] > map[popV[j + 1]]:
                j += 1
            if map[popV[j]] < map[popV[j + 1]]:
                j += 1
                flag = True

        return True


L = Solution()
print(L.IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))