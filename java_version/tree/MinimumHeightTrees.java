package tree;

import java.util.*;

public class MinimumHeightTrees {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<Integer> leaves = new ArrayList<>();
        if(n == 1){
            leaves.add(0);
            return leaves;
        }
        Set<Integer>[] adj = new HashSet[n];
        for(int i =0; i < n; i++){
            adj[i] = new HashSet<>();
        }

        for(int[] edge: edges){
            adj[edge[0]].add(edge[1]);
            adj[edge[1]].add(edge[0]);
        }

        for(int i = 0; i < n; i++){
            if(adj[i].size() == 1){
                leaves.add(i);
            }
        }

        while (n > 2){
            List<Integer> newLeaves = new ArrayList<>();
            n -= leaves.size();
            for(int i: leaves){
                int j = adj[i].iterator().next();
                adj[j].remove(i);
                if(adj[j].size() == 1){
                    newLeaves.add(j);
                }
            }
            leaves = newLeaves;
        }
        return leaves;
    }
}
