package bfs;

import java.util.HashMap;

public class Union_find_Graph_valid_tree {

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
    public boolean validTree(int n, int[][] edges) {
        if(n == 0){
            return false;
        }
        if(n == 1 && edges.length == 0){
            return false;
        }
        if(n-1 != edges.length){
            return false;
        }

        UnionFind unionFind = new UnionFind(n);
        for(int i =0; i < edges.length; i++){
            if(unionFind.find(edges[i][0]) == unionFind.find(edges[i][1])){
                return false;
            }
            unionFind.connect(edges[i][0], edges[i][1]);
        }
        return true;

    }
}
