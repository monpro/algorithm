class UnionFind(object):
    def __init__(self, edges):
        self.parent = [0] * len(edges)
    
    def find(self, x):
        if self.parent[x] == 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        self.parent[rootX] = rootY
        return True
    
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        unionFindIns = UnionFind(edges)
        
        for x, y in edges:
            if not unionFindIns.union(x - 1, y - 1):
                return [x, y]
        
        