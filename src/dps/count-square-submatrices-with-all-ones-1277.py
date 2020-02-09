class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        result = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] > 0 and i > 0 and j > 0:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                result += matrix[i][j]
        return result