# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        hash_dict = dict()
        for i in data:
            if i not in hash_dict:
                hash_dict[i] = 1
            else:
                hash_dict[i] += 1
        if k not in hash_dict:
            return 0

        return hash_dict[k]