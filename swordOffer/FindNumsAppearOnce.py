# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        hash_dict = dict()
        for i in array:
            if i not in hash_dict:
                hash_dict[i] = 1
            else:
                hash_dict[i] += 1

        result = []
        for i in hash_dict:
            if hash_dict[i] == 1:
                result.append(i)

        return result