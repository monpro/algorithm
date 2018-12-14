"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        #find all nodes
        if node is None:
            return None
        head = node
        visited = set([node])
        
        queue = [node]
        while queue != []:
            e = queue.pop(0)
            for i in e.neighbors:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        #get all nodes        
        nodes = visited
        mapping = {}
        #store old-new mapping in a hashmap
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        
        
        # copy neighbors(edges)
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
        
        return mapping[head]

                        
            
