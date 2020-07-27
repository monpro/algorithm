package backtraces;

import java.util.*;

class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        path.add(0);
        
        dfs(graph, 0, path, result);
        return result;
    }
    
    public void dfs(int[][] graph, int index, List<Integer> path, List<List<Integer>> result){
        if(index == graph.length - 1){
            result.add(new ArrayList<>(path));
            return;
        }
        
        for(int next: graph[index]){
            path.add(next);
            dfs(graph, next, path, result);
            path.remove(path.size() - 1);
        }
    }
}