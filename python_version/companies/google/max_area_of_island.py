class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        #BFS
        direction = [
            [0,1],
            [1,0],
            [0,-1],
            [-1,0]
        ]
        stack = []
        result = 0
        max_result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    stack.append([i,j])
                    grid[i][j] = 0
                    while len(stack) > 0:
                        node = stack.pop()
                        result += 1
                        for direc in direction:
                            if self.in_bound(node,direc,grid):
                                stack.append([node[0] + direc[0], node[1] + direc[1]])
                                grid[node[0] + direc[0]][node[1]+direc[1]] = 0
                    max_result = max(max_result, result)
                    result = 0
        return max_result


    def in_bound(self,node,direction,grid):
        row = node[0] + direction[0]
        column = node[1] + direction[1]
        return row < len(grid) and row >= 0 and column < len(grid[0]) \
               and column >= 0 and grid[row][column] == 1




