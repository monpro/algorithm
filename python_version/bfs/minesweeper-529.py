class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board
       
        x, y = click[0], click[1]
        if board[x][y] == "M":
            board[x][y] = "X"
        else:
            self.direction = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
            self.dfs(board, x, y)
        return board
    
    def inBound(self, i, j, m, n):
        if 0 <= i < m and 0 <= j < n:
            return True
        return False
    
    def dfs(self, board, x, y):
        if board[x][y] != 'E':
            return
        count = 0
        m, n = len(board), len(board[0])
        for i, j in self.direction:
            if self.inBound(i + x, j + y, m, n):
                if board[i + x][j + y] == "M":
                    count += 1
        if count > 0:
            board[x][y] = str(count)
            return
        else:
            board[x][y] = 'B'
        
        for i, j in self.direction:
            if self.inBound(i + x, j + y, m, n):
                self.dfs(board, i + x, j + y)
        