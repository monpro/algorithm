package backtraces;

import java.util.*;

class Solution {
    public List<List<Integer>> getFactors(int n) {
        // 2 3 5 7
        List<List<Integer>> result = new ArrayList<>();
        if(n == 1){
            return result;
        }
        List<Integer> path = new ArrayList<>();
        
        dfs(n, 2, path, result, (int)Math.sqrt(n));
        return result;
    }
    
    public void dfs(int n, int num, List<Integer> path, List<List<Integer>> result, int upper){
        if(n == 1 && path.size() > 1){
            result.add(new ArrayList<>(path));
            return;
        }
        
        for(int i = num; i <= n; i++){
            if(i > upper){
                i = n;
            }
            if(n % i == 0){
                path.add(i);
                dfs(n / i, i, path, result, (int)Math.sqrt(n / i));
                path.remove(path.size() - 1);
            }
        }
        
    }
}