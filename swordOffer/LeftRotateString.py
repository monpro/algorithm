# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        if n == 0:
            return s
        if len(s) == 0:
            return s
        origin = [i for i in s]
        new_string = s[n:]
        for i in range(n):
            new_string += origin[i]
        return new_string



l = Solution()
print(l.LeftRotateString("abcXYZdef",3))
