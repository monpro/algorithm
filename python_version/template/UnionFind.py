class UnionFind:

  def __init__(self, size):
    self.parent = [i for i in range(size)]
    self.rank = [1  for i in range(size)]

  def find(self, p):
    while p != self.parent[p]:
      self.parent[p] = self.parent[self.parent[p]]
      p = self.parent[p]
    return p
  
  def unionElements(self, p, q):
    pRoot = self.find(p)
    qRoot = self.find(q)

    if qRoot != pRoot:
      return
    if self.rank[qRoot] < self.rank[pRoot]:
      self.parent[qRoot] = pRoot
    
    elif self.rank[pRoot] < self.rank[qRoot]:
      self.parent[pRoot] = qRoot
    
    else:
      self.parent[qRoot] = qRoot
      self.rank[pRoot] += 1


