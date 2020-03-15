class Solution {
    public int numBusesToDestination(int[][] routes, int S, int T) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        Set<Integer> busVisited = new HashSet<>();
        Set<Integer> stopVisited = new HashSet<>();
        for(int i = 0; i < routes.length; i++){
            for(int stop: routes[i]){
                map.computeIfAbsent(stop, k -> new ArrayList<>()).add(i);
            }
        }
        Queue<Integer> queue = new LinkedList<>();
        int result = 0;
        queue.offer(S);
        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i = 0; i < size; i++){
                int stop = queue.poll();
                if(stop == T)
                    return result;
                if(!map.containsKey(stop))
                    continue;
                stopVisited.add(stop);

                for(int bus: map.get(stop)){
                    if(busVisited.contains(bus))
                        continue;
                    busVisited.add(bus);
                    for(int j: routes[bus]){
                        if(stopVisited.contains(j))
                            continue;
                        queue.offer(j);
                        stopVisited.add(j);
                    }
                }
            }
            result += 1;
        }
            
        return -1;
    }
}