class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # use bfs to flood the board
        if not board or not board[0]:
            return
        rowLimit = len(board)
        columnLimit = len(board[0])
        for i in range(columnLimit):
          if board[0][i] == 'O':
            self.dfs(board, 0, i)
          if board[rowLimit - 1][i] == 'O':
            self.dfs(board, rowLimit - 1, i)
        
        for j in range(rowLimit):
          if board[j][0] == 'O':
            self.dfs(board, j, 0)
          if board[j][columnLimit - 1]:
            self.dfs(board, j, columnLimit - 1)

        for i in range(rowLimit):
          for j in range(columnLimit):
            if board[i][j] == 'O':
              board[i][j] = 'X'
            if board[i][j] == '*':
              board[i][j] = 'O'
    def dfs(self, board, row, column):
      rowLimit = len(board)
      columnLimit = len(board[0])
      if row < 0 or row >= rowLimit or column < 0 or column >= columnLimit:
        return
      if board[row][column] == 'X' or board[row][column] == '*':
        return 
      board[row][column] = '*'
      self.dfs(board, row + 1, column)
      self.dfs(board, row - 1, column)
      self.dfs(board, row, column + 1)
      self.dfs(board, row, column - 1)     