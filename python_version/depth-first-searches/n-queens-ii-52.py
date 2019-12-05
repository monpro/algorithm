class Solution:
    def __init__(self):
      self.count = 0
    def totalNQueens(self, n):
      colIndex = [0 for i in range(n)]
      rowColIndex = [0 for i in range(2*n)]
      colRowIndex = [0 for i in range(2*n)]
      self.helper(0, n, colIndex, rowColIndex, colRowIndex)
      return self.count
    
    def helper(self, rowIndex, n, colIndex, rowColIndex, colRowIndex):
        if rowIndex == n:
          self.count += 1
        for col in range(n):
          id1 = col + rowIndex
          id2 = n - rowIndex + col
          if colIndex[col] or rowColIndex[id1] or colRowIndex[id2]:
            continue
          colIndex[col], rowColIndex[id1], colRowIndex[id2] = 1, 1, 1
          self.helper(rowIndex + 1, n, colIndex, rowColIndex, colRowIndex)
          colIndex[col], rowColIndex[id1], colRowIndex[id2] = 0, 0, 0
