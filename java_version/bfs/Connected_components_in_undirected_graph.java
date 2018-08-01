package bfs;

import java.util.*;

public class Connected_components_in_undirected_graph {


    class UnionFind{
        private int[] father = null;
        UnionFind(int n){
            father = new int[n + 1];
            for (int i = 1; i <= n; ++i)
                father[i] = i;
        }
        private int find(int x) {
            if (father[x] == x) {
                return x;
            }
            return father[x] = find(father[x]);
        }

        public void connect(int a, int b) {
            int root_a = find(a);
            int root_b = find(b);
            if (root_a != root_b)
                father[root_a] = root_b;
        }
    }
    public int countComponents(int n, int[][] edges) {
        Map<Integer, ArrayList<Integer>> map = new HashMap<>();
        //store the graph in hashmap
        for(int i = 0; i < n; i++){
            map.put(i,new ArrayList<>());
        }

        for(int[] edge: edges){
            map.get(edge[0]).add(edge[1]);
            map.get(edge[1]).add(edge[0]);
        }
        int result = n;
        UnionFind unionFind = new UnionFind(n);
        for(int[] edge:edges){
            if (unionFind.find(edge[0]) != unionFind.find(edge[1])) {
                unionFind.connect(edge[0],edge[1]);
                result -= 1;
            }
        }

        return result;
    }

    public int countComponents_bfs(int n, int[][] edges) {
        Map<Integer, ArrayList<Integer>> map = new HashMap<>();
        //store the graph in hashmap
        for(int i = 0; i < n; i++){
            map.put(i,new ArrayList<>());
        }

        for(int[] edge: edges){
            map.get(edge[0]).add(edge[1]);
            map.get(edge[1]).add(edge[0]);
        }

        //此时用BFS 需要VISITED
        boolean[] visited = new boolean[n + 1];
        for(int i = 0; i <= n; i++){
            visited[i] = false;
        }

        int result = 0;
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                Queue<Integer> queue = new LinkedList<>();
                queue.add(i);
                result += 1;
                while (!queue.isEmpty()){
                    int node = queue.poll();
                    visited[node] = true;
                    for(int neighboor: map.get(node)){
                        if(!visited[neighboor]){
                            queue.add(neighboor);
                        }
                    }
                }
            }
        }

        return result;
    }
}
