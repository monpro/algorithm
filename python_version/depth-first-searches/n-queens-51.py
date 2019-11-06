class Solution:
    def solveNQueens(self, n):
      if n <= 0:
        return []
      result = []
      self.helper(n, result, [])
      return result
    
    def helper(self, n, result, subset):
      if len(subset) == n:
        result.append(self.drawDassBoard(subset))
        return
      for i in range(n):
        if not self.isValid(subset, i):
          continue
        subset.append(i)
        self.helper(n, result, subset)
        subset.pop()
        


    def isValid(self, subset, index):
      rowSize = len(subset)
      for i in range(len(subset)):
        if subset[i] == index:
          return False
        elif i + subset[i] == rowSize + index:
          return False
        elif i - subset[i] == rowSize - index:
          return False
      
      return True


    def drawDassBoard(self, subset):
      dassBoard = []
      row = ""
      for i in subset:
        for j in range(len(subset)):
          if j == i:
            row += 'Q'
          else:
            row += '.'
        dassBoard.append(row)
        row = ''
      return dassBoard