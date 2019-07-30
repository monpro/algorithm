# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False

        root = sequence[-1]
        for i in range(len(sequence)):
            if sequence[i] > root:
                break

        for j in range(i, len(sequence)):
            if sequence[j] < root:
                return False

        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        right = True
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i: -1])

        return left and right
