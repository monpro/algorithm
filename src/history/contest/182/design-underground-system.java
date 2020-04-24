class UndergroundSystem {
    Map<Integer, Pair<String, Integer>> checkIn = new HashMap<>();
    Map<String, Pair<Integer, Integer>> checkOut = new HashMap<>();
    public UndergroundSystem() {
    }
    
    public void checkIn(int id, String stationName, int t) {
        checkIn.put(id, new Pair<>(stationName, t));
    }
    
    public void checkOut(int id, String stationName, int t) {
        Pair<String, Integer> pair = checkIn.get(id);
        String route = pair.getKey() + "->" + stationName;
        int totalTime = t - pair.getValue();
        Pair<Integer, Integer> checkout = checkOut.getOrDefault(route, new Pair<>(0, 0));
        checkOut.put(route, new Pair<>(checkout.getKey() + totalTime, checkout.getValue() + 1));
    }
    
    public double getAverageTime(String startStation, String endStation) {
        String route = startStation + "->" + endStation;
        Pair<Integer, Integer> pair = checkOut.get(route);
        
        return (double) pair.getKey() / pair.getValue();
    }
}