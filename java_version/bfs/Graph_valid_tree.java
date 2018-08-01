package bfs;

import java.util.*;

public class Graph_valid_tree {


    public Map<Integer, Set<Integer>> initmap(int n, int[][] edges){
        Map<Integer, Set<Integer>> map = new HashMap<>();
        for(int i = 0; i < n; i++){
            map.put(i, new HashSet<>());
        }


        for(int i = 0; i < edges.length;i++){
            int start = edges[i][0];
            int end = edges[i][1];
            map.get(start).add(end);
            map.get(end).add(start);
        }

        return map;

    }
    public boolean validTree(int n, int[][] edges) {
        if(n == 0){
            return true;
        }
        if(n != edges.length + 1){
            return false;
        }

        Map<Integer, Set<Integer>> map = initmap(n, edges);
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> set = new HashSet<>();
        queue.add(0);

        while(!queue.isEmpty()){
            int node =queue.poll();
            for(Integer integer: map.get(node)){
                if(set.contains(integer)){
                    continue;
                }
                set.add(integer);
                queue.add(integer);
            }

        }


    return (set.size() == n);


    }
}
