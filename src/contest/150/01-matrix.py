class Solution:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                left, up = float("Inf"), float("Inf")
                if i > 0:
                    left = matrix[i - 1][j]
                
                if j > 0:
                    up = matrix[i][j - 1]
                matrix[i][j] = min(left, up) + 1 
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == 0:
                    continue
                
                right, down = float("Inf"), float("Inf")
                if i < m - 1:
                    right = matrix[i + 1][j]
                if j < n - 1:
                    down = matrix[i][j + 1]
                matrix[i][j] = min(matrix[i][j], min(right, down) + 1)
        
        return matrix