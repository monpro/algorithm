package bfs;

import java.util.*;

public class course_schedule_ii {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // write your code here
        ArrayList<Integer> result = new ArrayList<>();

        if(numCourses == 0){
            int[] array = result.stream().mapToInt(i->i).toArray();
            return array;
        }
        if(prerequisites.length == 0){
            for(int i =0; i < numCourses; i++){
                result.add(i);

            }
            int[] array = result.stream().mapToInt(i->i).toArray();
            return array;
        }
        Map<Integer, Integer> map = new LinkedHashMap<>();
        Map<Integer, ArrayList<Integer>> neighboors = new LinkedHashMap<>();
        for(int i = 0 ; i < numCourses;i++){
            neighboors.put(i, new ArrayList<>());
        }
        for(int[] elements: prerequisites){
            int start = elements[1];
            int end = elements[0];
            if(map.containsKey(end)){
                map.put(end, map.get(end) + 1);
            }
            else{
                map.put(end, 1);
            }
            neighboors.get(start).add(end);
        }
        Queue<Integer> queue = new LinkedList<>();
        for(int i =0; i < numCourses; i++){
            if(!map.containsKey(i)){
                queue.add(i);
                result.add(i);
            }
        }

        while(!queue.isEmpty()){
            Integer node = queue.poll();
            for(Integer neighboor : neighboors.get(node)){
                map.put(neighboor, map.get(neighboor) - 1);
                if(map.get(neighboor) == 0){
                    queue.add(neighboor);
                    result.add(neighboor);
                }
            }
        }

        if(result.size() == numCourses){
            return result.stream().mapToInt(i->i).toArray();
        }
        else{
            int[] new_array = new int[0];
            return new_array;
        }

    }
}
