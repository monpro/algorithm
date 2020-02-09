class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
          return 0
        row_length, col_length = len(matrix), len(matrix[0])
        cache = [[0 for i in range(col_length)] for j in range(row_length)]
        result = 1
        for i in range(row_length):
          for j in range(col_length):
            result = max(result, self.helper(matrix, i, j, cache, row_length, col_length))
        return result

    def helper(self, matrix, row, column, cache, row_length, col_length):
      if cache[row][column] != 0:
        return cache[row][column]
      direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]
      temp = 1
      for i in direction:
        new_row, new_col = row + i[0], column + i[1]
        if not self.inBound(new_row, new_col, row_length, col_length) or matrix[new_row][new_col] <= matrix[row][column]:
          continue
        temp = max(temp, 1 + self.helper(matrix, new_row, new_col, cache, row_length, col_length))
      cache[row][column] = temp
      return temp

    def inBound(self,row, column, row_length, col_length):
      return 0 <= row and row < row_length and 0 <= column and column < col_length