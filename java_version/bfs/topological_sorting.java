package bfs;

import java.util.*;

public class topological_sorting {
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {

        ArrayList<DirectedGraphNode> result = new ArrayList<>();
        if(graph == null){
            return result;
        }
        //use hashmap to store
        Map<DirectedGraphNode, Integer> map = new HashMap<>();
        for(DirectedGraphNode directedGraphNode: graph){
            for(DirectedGraphNode neighboor: directedGraphNode.neighbors){
                if (map.containsKey(neighboor)){
                    map.put(neighboor, map.get(neighboor) + 1);

                }
                else{
                    map.put(neighboor, 1);
                }
            }
        }
        //queue store all node 入度 = 0
        Queue<DirectedGraphNode> queue = new LinkedList<>();
        for(DirectedGraphNode directedGraphNode: graph){
            if(!map.containsKey(directedGraphNode)){
                queue.add(directedGraphNode);
                result.add(directedGraphNode);
            }
        }

        while (!queue.isEmpty()){
            DirectedGraphNode node = queue.poll();
            for(DirectedGraphNode directedGraphNode: node.neighbors){
                map.put(directedGraphNode,map.get(directedGraphNode) - 1);
                if(map.get(directedGraphNode) == 0){
                    result.add(directedGraphNode);
                    queue.add(directedGraphNode);
                }
            }
        }
        return result;
    }
}
