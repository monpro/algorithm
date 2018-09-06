# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        root = sequence[-1]

        for i in range(len(sequence)):
            if sequence[i] > root:
                break

        for j in range(i + 1, len(sequence)):
            if sequence[j] < root:
                return False

        left, right = True, True

        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0:i])

        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])


        return left and right