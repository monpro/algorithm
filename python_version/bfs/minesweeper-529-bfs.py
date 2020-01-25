class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board
        x, y = click[0], click[1]
        if board[x][y] == "M":
            board[x][y] = "X"
        else:
            direction = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
            m, n = len(board), len(board[0])
            stack = [[x, y]]
            while len(stack) > 0:
                [x, y] = stack.pop(0)
                count = 0
                for i, j in direction:
                    next_x, next_y = i + x, j + y
                    if 0 <= next_x < m and 0 <= next_y < n:
                        if board[next_x][next_y] == 'M':
                            count += 1     
                if count == 0:
                    board[x][y] = 'B'
                    for i, j in direction:
                        next_x, next_y = i + x, j + y
                        if 0 <= next_x < m and 0 <= next_y < n:
                            if board[next_x][next_y] == 'E':
                                stack.append([next_x, next_y])
                                board[next_x][next_y] = 'B'
                else:
                    board[x][y] = str(count)
                    
        return board
                            
                            
                        
            