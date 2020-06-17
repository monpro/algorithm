class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        matrix = [[0] * n for i in range(n)]
        rowBegin, colBegin, rowEnd, colEnd = 0, 0, n - 1, n - 1
        num = 1
        while rowBegin <= rowEnd and colBegin <= colEnd:
            for i in range(colBegin, colEnd + 1):
                matrix[rowBegin][i] = num
                num += 1
            rowBegin += 1
            for i in range(rowBegin, rowEnd + 1):
                matrix[i][colEnd] = num
                num += 1
            colEnd -= 1
            for i in range(colEnd, colBegin - 1, -1):
                matrix[rowEnd][i] = num
                num += 1
            rowEnd -= 1

            for i in range(rowEnd, rowBegin - 1, -1):
                matrix[i][colBegin] = num
                num += 1
            colBegin += 1

        return matrix
