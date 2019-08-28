class Solution:
    def generate(self, numRows):
        if numRows == 0:
          return 0
        if numRows == 1:
          return [[1]]
        if numRows == 2:
          return [[1], [1, 1]]
        result = [[1], [1, 1]]
        temp = []
        for i in range(2, numRows):
          temp.append(1)
          for j in range(1, i):
            temp.append(result[i - 1][j - 1] + result[i - 1][j])
          temp.append(1)
          result.append(temp)
          temp = []
        return result

