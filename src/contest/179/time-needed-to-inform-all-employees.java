class Solution {
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        Map<Integer, List<Integer>> subordinates = new HashMap<>();
        int total = 0;
        for(int i = 0; i < manager.length; i++){
            int j = manager[i];
            List<Integer> subord = subordinates.getOrDefault(j, new ArrayList<>());
            subord.add(i);
            subordinates.put(j, subord);
        }
        return dfs(subordinates,headID, informTime);
    }
    
    public int dfs(Map<Integer, List<Integer>> graph, int id, int[] informTime){
        int maxVal = 0;
        if(!graph.containsKey(id))
            return 0;
        for(int i = 0; i < graph.get(id).size(); i++){
            maxVal = Math.max(maxVal, dfs(graph, graph.get(id).get(i), informTime));
        }
        
        return maxVal + informTime[id];
        
    }
}