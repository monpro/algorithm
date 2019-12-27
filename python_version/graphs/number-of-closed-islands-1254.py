class Solution:
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1 :
                    self.flood(grid, i, j)
        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    result += 1
                    self.flood(grid, i, j)
        
        return result
    
    
    def flood(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])
        if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 1:
            return 
        grid[i][j] = 1
        for direction in self.directions:
            self.flood(grid, i + direction[0], j + direction[1])