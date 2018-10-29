package bfs;

import java.util.LinkedList;
import java.util.Queue;

class Point{
    int x;
    int y;
    Point(){
        this.x = 0;
        this.y = 0;
    }
    Point(int x, int y){
        this.x = x;
        this.y = y;
    }
}
public class Knight_shortest_path {
    public int shortestPath(boolean[][] grid, Point source, Point destination) {
        // write your code here
        if(grid.length == 0 || grid[0].length == 0){
            return -1;
        }
        if(source.x == destination.x && source.y == destination.y){
            return 0;
        }
        int result = -1;
        result = helper(grid, source, destination);
        return result;

    }
    public boolean inBound(boolean[][] grid, Point source, int[] element){
        return source.x + element[0] >= 0 && source.x + element[0] < grid.length &&
                source.y + element[1] >= 0 && source.y + element[1] < grid[0].length;
    }
    public int helper(boolean[][] grid, Point source, Point destination){
        int[][] matrix = {{1,2},{1,-2},{-1,2},{-1,-2},{2,1},{2,-1},{-2,1},{-2,-1}};
        Queue<Point> queue = new LinkedList<>();
        int result = 0;
        grid[source.x][source.y] = true;
        queue.add(source);
        while(!queue.isEmpty()){
            int size = queue.size();
            result += 1;
            for(int i=0; i < size;i++){
                Point point = queue.poll();
                for(int[] element: matrix){
                    if(inBound(grid, point, element)) {
                        if(!grid[point.x + element[0]][point.y + element[1]]) {
                            grid[point.x + element[0]][point.y + element[1]] = true;
                            queue.add(new Point(point.x + element[0], point.y + element[1]));
                            if (point.x + element[0] == destination.x && point.y + element[1] == destination.y) {
                                return result;
                            }
                        }
                    }
                }
            }

        }
        return -1;
    }
}
