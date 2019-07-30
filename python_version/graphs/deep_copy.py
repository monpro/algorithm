"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """

    @staticmethod
    def cloneGraph(node):
        if node is None:
            return None
        head = node
        visited = {node}
        queue = [node]
        while queue:
            e = queue.pop(0)
            for i in e.neighbors:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

        nodes = visited
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)

        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
        
        return mapping[head]

