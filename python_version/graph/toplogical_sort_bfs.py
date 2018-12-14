"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # write your code here
        # indegree_hash_map for every node
        indegree_hash_map = dict((i, 0) for i in graph)
        for i in indegree_hash_map:
            for j in i.neighbors:
                indegree_hash_map[j] += 1
        queue, result = [], []
        # get all 0- degree-node
        for i in indegree_hash_map:
            if indegree_hash_map[i] == 0:
                queue.append(i)
        while queue != []:
            node = queue.pop(0)
            result.append(node)
            for i in node.neighbors:
                indegree_hash_map[i] -= 1
                if indegree_hash_map[i] == 0:
                    queue.append(i)

        return result
