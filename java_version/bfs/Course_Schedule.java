package bfs;

import java.util.*;

public class Course_Schedule {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // write your code here
        Map<Integer, Integer> map = new HashMap<>();
        Map<Integer, ArrayList<Integer>> neighboors = new HashMap<>();
        for(int i =0 ; i < numCourses; i++){
            neighboors.put(i, new ArrayList<>());
        }
        boolean result = true;
        ArrayList<Integer> toCheck = new ArrayList<>();
        if(numCourses == 0 || prerequisites.length == 0){
            return false;
        }
        for(int[] element: prerequisites){
            int end = element[0];
            int start = element[1];
            if (map.containsKey(end)) {
                map.put(end, map.get(end) + 1);
            }
            else{
                map.put(end, 1);
            }
            neighboors.get(start).add(end);
        }
        Queue<Integer> queue = new LinkedList<>();

        for(int i = 0 ; i < numCourses; i++){
            if(!map.containsKey(i)){
                queue.add(i);
                toCheck.add(i);
            }
        }
        while(!queue.isEmpty()){
            Integer node =queue.poll();
            for(Integer integer: neighboors.get(node)){
                map.put(integer, map.get(integer) -1);
                if(map.get(integer) == 0){
                    toCheck.add(integer);
                    queue.add(integer);
                }
            }
        }
        return toCheck.size() == numCourses;
    }
}
