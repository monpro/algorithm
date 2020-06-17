class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        # write your code here
        if grid == []:
            return 0

        delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        queue = []
        row, column = len(grid), len(grid[0])
        result = 0

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    queue.append((i, j))

        # the process of bfs
        while queue != []:

            next_day_queue = []

            for i, j in queue:
                for dx, dy in delta:
                    if 0 <= i + dx < row and 0 <= j + dy < column and grid[i + dx][j + dy] == 0:
                        next_day_queue.append((i + dx, j + dy))
                        grid[i + dx][j + dy] = 1

            result += 1
            queue = next_day_queue

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 0:
                    return -1

        return result - 1