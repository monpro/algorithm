package bfs;

import java.util.*;

public class clone_graph {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null) {
            return null;
        }

        UndirectedGraphNode root = new UndirectedGraphNode(node.label);
        Map<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<>();
        Set<UndirectedGraphNode> set = new HashSet<>();
        Queue<UndirectedGraphNode> queue = new LinkedList<>();
        queue.add(node);
        set.add(node);
        map.put(node, root);
        //store the relationship node - newnode with same label-- set contains all node
        while(!queue.isEmpty()){
            UndirectedGraphNode new_node = queue.poll();
            for(UndirectedGraphNode neighboor: new_node.neighbors){
                if(set.contains(neighboor)){
                    continue;
                }
                set.add(neighboor);
                queue.add(neighboor);
                map.put(neighboor, new UndirectedGraphNode(neighboor.label));
            }
        }
        for(UndirectedGraphNode undirectedGraphNode:set){
            UndirectedGraphNode new_node  = map.get(undirectedGraphNode);
            for(UndirectedGraphNode neighboor: undirectedGraphNode.neighbors){
                new_node.neighbors.add(map.get(neighboor));
            }
        }

        return map.get(node);


    }
}
