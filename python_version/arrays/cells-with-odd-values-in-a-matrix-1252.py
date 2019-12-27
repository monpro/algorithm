class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rowBoolean = [0 for _ in range(n)]
        colBoolean = [0 for _ in range(m)]
        rowNum, colNum = 0, 0
        for indice in indices:
            rowIndice, colIndice = indice[0], indice[1]
            rowBoolean[rowIndice] ^= 1
            colBoolean[colIndice] ^= 1
            
            rowNum += 1 if rowBoolean[rowIndice] == 1 else -1
            colNum += 1 if colBoolean[colIndice] == 1 else -1
        
        return (m - colNum) * rowNum + (n - rowNum) * colNum