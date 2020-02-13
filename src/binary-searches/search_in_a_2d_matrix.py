class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        row, column = 0, len(matrix[0]) - 1
        right_up = matrix[row][column]
        while 0 <= row < len(matrix) and 0 <= column < len(matrix[0]):
            right_up = matrix[row][column]
            if target < right_up:
                column -= 1
            elif target > right_up:
                row += 1
            elif target == right_up:
                return True

        return False