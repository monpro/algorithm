class Solution(object):

    def __init__(self):
      self.result = 0
      self.directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(len(A[0])):
          if A[0][i] == 1:
            self.flood(A, 0, i)
          if A[-1][i] == 1:
            self.flood(A, len(A) - 1, i)
        for i in range(len(A)):
          if A[i][0] == 1:
            self.flood(A, i, 0)
          if A[i][-1] == 1:
            self.flood(A, i , len(A[0]) - 1)
        result = 0
        for row in A:
          for e in row:
            if e == 1:
              result += 1
        return result

    def flood(self, A, row, col):
      if not self.inBound(A, row, col):
        return
      A[row][col] = 0
      for (i, j) in self.directions:
        if self.inBound(A, row + i, col + j):
          if A[row + i][col + j] == 1:
              A[row + i][col + j] = 0
              self.flood(A, row + i, col + j)

    def inBound(self, A, row, col):
      if 0 <= row < len(A) and 0 <= col < len(A[0]):
        return True
      else:
        return False 

if __name__ == "__main__":
    l = Solution()
    print(l.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))