# -*- coding:utf-8 -*-
class Solution:
    class Solution:
        def printMatrix(self, matrix):
            if not matrix or not matrix[0]:
                return matrix
            result = []
            while matrix:
                result += matrix.pop(0)
                if not matrix or not matrix[0]:
                    break
                matrix = self.helper(matrix)

            return result

        def helper(self, matrix):
            new_matrix = []
            len_row = len(matrix)
            len_col = len(matrix[0])

            row = []
            for i in range(len_col):
                for j in range(len_row):
                    row.append(matrix[j][i])
                new_matrix.append(row)
                row = []
            new_matrix.reverse()
            return new_matrix
