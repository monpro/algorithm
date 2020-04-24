class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # critical connections is composed of points only visted once
        graph = [[] for i in range(n)]
        
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        lowest = [-1] * n
        result = []
        
        def dfs(node, current_depth, parent):
            if lowest[node] == -1:
                lowest[node] = current_depth
                
                for neighbor in graph[node]:
                    if neighbor != parent:
                        neighborDepth = current_depth + 1
                        actualDepth = dfs(neighbor, neighborDepth, node)

                        if actualDepth >= neighborDepth:
                            result.append((node, neighbor))


                        lowest[node] = min(lowest[node], actualDepth)
                    
            return lowest[node]
        
        dfs(0, 0, -1)
        return result