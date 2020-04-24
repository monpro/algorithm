class Solution {
    public int totalFruit(int[] tree) {
        int[] visited = new int[tree.length];
        int start = 0, result = 0;
        int count = 0;
        
        for(int end = 0; end < tree.length; end++){
            if(visited[tree[end]] == 0){
                count += 1;
            }
            
            visited[tree[end]] += 1;
            
            while(count > 2){
                visited[tree[start]] -= 1;
                
                if(visited[tree[start]] == 0){
                    count -= 1;
                }
                
                start += 1;
            }
            
            result = Math.max(result, end - start + 1);
        }
        
        return result;
    }
}