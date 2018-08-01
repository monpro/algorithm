package dfs;

import java.util.*;

public class word_ladder {
    public int ladderLength(String start, String end, Set<String> dict) {
        // write your code here
        int result = 0;
        if(start.equals(end)){
            return 1;
        }
        //this could use bfs
        Queue<String> queue = new LinkedList<>();
        queue.add(start);
        while(!queue.isEmpty()){
            int size = queue.size();
            result += 1;
            for(int i = 0; i < size;i++){
                String node = queue.poll();
                if(node.equals(end)){
                    return result;
                }
                List<String> next = findNextAndRemove(dict, node);
                for(String string:next){
                    if(string.equals(end)){
                        result += 1;
                        return result;
                    }
                    queue.add(string);

                }
            }
        }
        return result;
    }

    List<String> findNextAndRemove(Set<String> dict, String node){
        List<String> list = new ArrayList<>();
        for(String string: dict){
            int difference = 0;
            for(int i = 0 ; i < node.length();i++){
                if(string.charAt(i) != node.charAt(i)){
                    difference += 1;
                }
            }
            if(difference == 1){
                list.add(string);
            }
        }
        dict.removeAll(list);
        return list;
    }
    boolean isNeighboor(String node, String neighboor){
        int difference = 0;
        int size = node.length();
        for(int i = 0; i < size; i++){
            if(node.charAt(i) != neighboor.charAt(i)){
                difference += 1;
            }
        }
        if(difference == 1){
            return true;
        }
        else{
            return false;
        }

    }
}
