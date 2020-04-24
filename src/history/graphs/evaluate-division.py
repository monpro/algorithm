class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.buildGraph(equations, values)
        result = []
        for query in queries:
            [source, final] = query
            if source not in graph or final not in graph:
                result.append(-1.0)
                continue
            
            queue = [[source, 1.0]]
            visited = set()
            product = -1.0
            while queue:
                node, figure = queue.pop(0)
                if node == final:
                    product = figure
                visited.add(node)
                for i, val in graph[node]:
                    if i not in visited:
                        queue.append((i, val * figure))
            result.append(product)
        return result
    
    def buildGraph(self, equations, values):
        graph = collections.defaultdict(list)
        n = len(equations)
        for i in range(n):
            [source, final] = equations[i]
            dist = values[i]
            graph[source].append((final, dist))
            graph[final].append((source, 1 / dist))

        return graph
    