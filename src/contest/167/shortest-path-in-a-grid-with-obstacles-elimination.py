from collections import deque
class Solution:
    def shortestPath(self, grid, k):
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        queue = deque([(0, 0, 0)])
        visited = {(0, 0): 0}
        step = 0
        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                row, col, elinimate = queue.popleft()
                if elinimate > k:
                    continue
                if row == m - 1 and col == n - 1:
                    return step
                for i, j in [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]:
                    if 0 <= i < m and 0 <= j < n:
                        if grid[i][j] == 1:
                            next_elinimate = elinimate + 1
                        else:
                            next_elinimate = elinimate
                        if next_elinimate < visited.get((i, j), float("inf")):
                            visited[(i, j)] = next_elinimate
                            queue.append((i, j, next_elinimate))
            step += 1
        return -1
