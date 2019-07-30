class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        '''
        if len(M) == 0 or len(M[0]) == 0:
            return 0
        stack,result = [],0
        direction = [
            [0,1],
            [1,0],
            [0,-1],
            [-1,0]
        ]
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j] == 1:
                    stack.append([i,j])
                    M[i][j] = 0
                    while len(stack) > 0:
                        node = stack.pop()
                        for direc in direction:
                            if self.in_bound(M,node,direc):
                                row, column = node[0] + direc[0], node[1] + direc[1]
                                stack.append([row,column])
                                M[row][column] = 0
                    result += 1
        return result



    def in_bound(self,M,element,direction):
        row = element[0] + direction[0]
        column = element[1] + direction[1]

        return 0<= row < len(M) and 0<= column < len(M[0]) and M[row][column] == 1
    '''
        graph = dict()
        visited = set()
        result = 0
        for i in range(len(M)):
            graph[M[i]] = []
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    graph[i].append(j)

        def dfs(node):
            if node not in visited:
                visited.add(node)
                for i in graph[node]:
                    dfs(i)

        for i in range(len(M)):
            if i not in visited:
                dfs(i)
                result += 1

        return result







