class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # dps[i][j], grid[i - 1][j - 1] distance to closest 1
        m, n = len(grid), len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    continue
                
                grid[i][j] = float("Inf")
                if i > 0:
                    grid[i][j] = min(grid[i][j], grid[i - 1][j] + 1)
                if j > 0:
                    grid[i][j] = min(grid[i][j], grid[i][j - 1] + 1)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1: 
                    continue
                 
                if i < m - 1:
                    grid[i][j] = min(grid[i][j], grid[i + 1][j] + 1)
                if j < m - 1:
                    grid[i][j] = min(grid[i][j], grid[i][j + 1] + 1)
                result = max(result, grid[i][j])
        return -1 if result == float('Inf') else result - 1