class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n == 0:
            return False
        # if #edges == n - 1
        if len(edges) != n - 1:
            return False
        if n == 1 and len(edges) == 0:
            return True
        
        adjacency_list = {}
        for edge in edges:
            adjacency_list[edge[0]] = []
            adjacency_list[edge[1]] = []
        for edge in edges:
            adjacency_list[edge[0]] = adjacency_list[edge[0]] + [edge[1]]
            adjacency_list[edge[1]] = adjacency_list[edge[1]] + [edge[0]]
        queue,visited = [0],set([0])
        while queue != []:
            e = queue.pop(0)
            for node in adjacency_list[e]:
                if node in visited:
                    continue
                queue.append(node)
                visited.add(node)
        print(len(visited))
        if len(visited) == n:
            return True
        else:
            return False
                        
            
