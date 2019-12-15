class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i - 1][j - 1]
    
        self.dp = dp


        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
        minRow, maxRow = min(row1, row2), max(row1, row2)
        minCol, maxCol = min(col1, col2), max(col1, col2)

        return self.dp[maxRow + 1][maxCol + 1] - self.dp[maxRow + 1][minCol] \
            - self.dp[minRow][maxCol + 1] + self.dp[minRow][minCol]


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)