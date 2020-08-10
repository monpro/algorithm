class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:        
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[0 for i in range(len(maze[0]))] for j in range(len(maze))]
        return self.dfs(maze, visited, start, destination)
    
    def dfs(self, maze, visited, start, dest):
        if visited[start[0]][start[1]]:
            return False
        if start[0] == dest[0] and start[1] == dest[1]:
            return True
        visited[start[0]][start[1]] = 1
        for direction in self.directions:
            nextStart = self.getNextStart(maze, start[0], start[1], direction)
            if self.dfs(maze, visited, nextStart, dest):
                return True
        return False
            
    
    def getNextStart(self, maze, row, col, direction):
        while self.canMove(maze, row + direction[0], col + direction[1]):
            row += direction[0]
            col += direction[1]
        return [row, col]
        
    def canMove(self, maze, nextRow, nextCol):
        if nextRow < 0 or nextRow >= len(maze) or nextCol < 0 or nextCol >= len(maze[0]):
            return False
        else:
            return maze[nextRow][nextCol] != 1