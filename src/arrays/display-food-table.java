package arrays;

import java.util.*;

class Solution {
    // {3: {Chicken: 1}}
    public List<List<String>> displayTable(List<List<String>> orders) {
        List<List<String>> result = new ArrayList<>();
        TreeMap<Integer, Map<String, Integer>> map = new TreeMap<>();
        TreeSet<String> dishes = new TreeSet<>();
        List<String> firstRow = new ArrayList<>();
        firstRow.add("Table");
        for(List<String> list: orders) {
            int table = Integer.parseInt(list.get(1));
            String dish = list.get(2);
            dishes.add(dish);
            map.putIfAbsent(table, new HashMap<>());
            Map<String, Integer> dishCount= map.get(table);
            dishCount.put(dish, dishCount.getOrDefault(dish, 0) + 1);
        }
        
        firstRow.addAll(dishes);
        result.add(firstRow);
        map.forEach((table, dishCount) -> {
            List<String> row = new ArrayList<>();
            row.add(String.valueOf(table));
            dishes.forEach(dish -> {
                row.add(String.valueOf(dishCount.getOrDefault(dish, 0)));
            });
            result.add(row);
        });
        return result;
    }
}