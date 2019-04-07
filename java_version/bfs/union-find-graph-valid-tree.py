
class UnionFind:
    def __init__(self, n):
        father = [i for i in range(n)]

    def find(self,x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def connect(self,a,b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_a

class Solution:
    def validTree(self,n,edges):
        if n == 0:
            return False
        if n == 1 and len(edges) == 0:
            return False
        if n - 1 != len(edges):
            return False
        #
        unionFind = UnionFind(n)
        for i in range(len(edges)):
            if unionFind.find(edges[i][0]) == unionFind.find(edges[i][1]):
                return False
            unionFind.connect(edges[i][0], edges[i][1])
        return True



