# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        hash = dict()
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        for i in range(len(s)):
            if hash[s[i]] == 1:
                return i


l = Solution()
l.FirstNotRepeatingChar("google")