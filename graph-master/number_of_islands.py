class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        # use bfs to search the grid

        if len(grid) == 0:
            return 0

        delat = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = len(grid), len(grid[0])
        result = 0

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, delat)
                    result += 1

        return result

    def bfs(self, grid, i, j, delat):
        queue = []
        queue.append((i, j))
        grid[i][j] = 0
        while len(queue) > 0:
            x, y = queue.pop(0)
            for dx, dy in delat:
                if 0 <= dx + x < len(grid) and 0 <= dy + y < len(grid[0]) and grid[dx + x][dy + y] == 1:
                    grid[dx + x][dy + y] = 0
                    queue.append((dx + x, dy + y))
