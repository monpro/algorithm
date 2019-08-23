class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # use bfs to flood the board
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for direction in directions:
          print(direction)
          
        