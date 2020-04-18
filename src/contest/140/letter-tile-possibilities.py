class Solution:
    count = 0
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = sorted(tiles)
        visited = [0 for _ in range(len(tiles))]
        self.dfs(tiles, visited, 0)
        
        return self.count
    
    
    def dfs(self, tiles, visited, index):
        if index == len(tiles):
            return
        
        for i in range(len(tiles)):
            if visited[i]:
                continue
            if i > 0 and tiles[i] == tiles[i - 1] and visited[i - 1] == 0:
                continue
            
            self.count += 1
            visited[i] = 1
            self.dfs(tiles, visited, index + 1)
            visited[i] = 0
            