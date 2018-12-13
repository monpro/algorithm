# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.dicrecion = [
            [0,1],
            [1,0],
            [0,-1],
            [-1,0]
        ]
    #backtrace core idea : use visited array
    def hasPath(self, matrix, rows, cols, path):
        # write code her
        visited = [0 for i in range(len(matrix))]
        for row in range(rows):
            for col in range(cols):
                if self.helper(matrix,rows,cols,row,col,visited,path,0):
                    return True

        return False

    def helper(self,matrix,rows,cols,row,col,visited,path,index):
        position = row * cols + col
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
        if matrix[position] != path[index] or visited[position]:
            return False
        if index == len(path) - 1:
            return True
        visited[position] = True
        for dir in self.dicrecion:
            if self.helper(matrix,rows,cols,row + dir[0],col + dir[1], [i for i in visited],path, index + 1):
                return True

        visited[position] = False
        return False




l = Solution()
print(l.hasPath("ABCESFCSADEE",3,4,"ABCB"))