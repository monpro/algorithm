# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.direction =[
            [0,1],
            [-1,0],
            [1,0],
            [0,-1]
        ]
    def movingCount(self, threshold, rows, cols):
        visited = [0 for _ in range(rows * cols)]
        print(visited)
        return self.helper(threshold,rows,cols,0,0,visited)

    def helper(self,threshold,rows,cols,row,col,visited):
        position = row * cols + col;
        if row >= rows or row < 0 or col < 0 or col >= cols or visited[position]:
            return 0
        number = str(row) + str(col)
        num = 0
        for i in number:
            num += int(i)
        if num > threshold:
            return 0
        visited[position] = True
        count = 0
        count += 1
        for dir in self.direction:
            count += self.helper(threshold,rows,cols,row + dir[0],col + dir[1],visited)
        return count




# write code here
l = Solution()
print(l.movingCount(5,10,10))