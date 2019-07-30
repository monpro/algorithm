# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return node

        queue = []
        visited = set()
        queue.append(node)
        original_new = dict()
        original_new[node] = UndirectedGraphNode(node.label)
        visited.add(node)
        while len(queue) > 0:
            node = queue.pop(0)
            for i in node.neighbors:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
                    original_new[i] = UndirectedGraphNode(i.label)

        for node in visited:
            for i in node.neighbors:
                original_new[node].append(original_new[i])

        return original_new[node]









