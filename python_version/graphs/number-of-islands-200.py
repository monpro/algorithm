class Solution(object):
    def numIslands(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        stack = []
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    stack.append([i, j])
                    grid[i][j] = 0
                    self.bfsGraph(directions, grid, stack)
                    result += 1
        return result

    def bfsGraph(self, directions, grid, stack):
        while len(stack) > 0:
            node = stack.pop()
            for direction in directions:
                if self.inBound(node, direction, grid):
                    stack.append([node[0] + direction[0], node[1] + direction[1]])
                    grid[node[0] + direction[0]][node[1] + direction[1]] = "0"

    def inBound(self, node, direction, grid):
        row = node[0] + direction[0]
        column = node[1] + direction[1]
        return len(grid) > row >= 0 and len(grid[0]) > column >= 0 and grid[row][column] == "1"