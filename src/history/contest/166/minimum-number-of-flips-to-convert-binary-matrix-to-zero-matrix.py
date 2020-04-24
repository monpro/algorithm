from copy import deepcopy
class Solution:
    def minFlips(self, mat):
        #mat = [[1,0,0],[1,0,0]]
        m = len(mat)
        n = len(mat[0])
        flatten = []
        for i in mat:
            flatten.extend(i)
        stack = [(flatten, 0)]
        visited = {}
        visited[tuple(flatten)] = True
        while len(stack) > 0:
            matrix, step = stack.pop(0)
            if sum(matrix) == 0:
                return step
            for i in range(m):
                for j in range(n):
                    temp = deepcopy(matrix)
                    direction = [[i, j], [i + 1, j],
                    [i - 1, j], [i, j + 1], [i, j - 1]]
                    for [x, y] in direction:
                        if x >= 0 and x < m and y >= 0 and y < n:
                            temp[x*n+y] = 0 if temp[x*n+y] else 1
                    if tuple(temp) not in visited:
                        stack.append((temp, step + 1))
                        visited[tuple(temp)] = True
        return -1

if __name__ == "__main__":
    mat = [[0,0],[0,1]]
    print(Solution().minFlips(mat))