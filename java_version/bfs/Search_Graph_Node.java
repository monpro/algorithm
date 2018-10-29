package bfs;

import java.util.*;

public class Search_Graph_Node {
    public UndirectedGraphNode searchNode(ArrayList<UndirectedGraphNode> graph, Map<UndirectedGraphNode, Integer> values, UndirectedGraphNode node, int target) {
        UndirectedGraphNode result = null;
        if (graph == null){
            return result;
        }
        //use bfs to find shortest distance
        Queue<UndirectedGraphNode> queue = new LinkedList<>();
        queue.add(node);
        HashSet<UndirectedGraphNode> visited = new LinkedHashSet<>();
        visited.add(node);

        while(!queue.isEmpty()){
            UndirectedGraphNode new_node = queue.poll();
            if(values.get(new_node) == target){
                return new_node;
            }

            for(UndirectedGraphNode undirectedGraphNode: new_node.neighbors){
                if(visited.contains(undirectedGraphNode)){
                    continue;
                }
                if(values.get(undirectedGraphNode) == target){
                    return undirectedGraphNode;
                }

                visited.add(undirectedGraphNode);
                queue.add(undirectedGraphNode);
            }
        }
        return null;
    }
}
