"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """

    def searchNode(self, graph, values, node, target):
        # write your code here

        if values == []:
            return None
        if values[node] == target:
            return node

        # use bfs
        queue, visited = [node], []
        while queue != []:
            e = queue.pop(0)
            visited.append(e)
            if values[e] == target:
                return e

            for i in e.neighbors:
                if i not in visited:
                    queue.append(i)

        return None



