package bfs;

import java.util.LinkedList;
import java.util.Queue;

class coordinate{
    int x;
    int y;
    public coordinate(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class number_of_islands {
    public int numIslands(boolean[][] grid) {
        // write your code here
        int result = 0;
        if(grid.length == 0 || grid[0].length == 0){
            return result;
        }

        for(int i =0; i < grid.length;i++){
            for(int j=0; j < grid[0].length;j++){
                if(grid[i][j]){
                    helper(grid,i,j);
                    result += 1;
                }
            }
        }

        return result;
    }

    public void helper(boolean[][] grid, int i, int j) {
        int[][] matrix = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        Queue<coordinate> queue = new LinkedList<>();
        grid[i][j] = false;
        queue.add(new coordinate(i, j));
        while (!queue.isEmpty()) {
            coordinate node = queue.poll();
            for (int[] element : matrix) {
                if (node.x + element[0] >= 0 && node.x + element[0] < grid.length &&
                        node.y + element[1] >= 0 && node.y + element[1] < grid[0].length) {
                    if (grid[node.x + element[0]][node.y + element[1]]) {
                        grid[node.x + element[0]][node.y + element[1]] = false;
                        queue.offer(new coordinate(node.x + element[0], node.y + element[1]));
                    }
                }
            }
        }
    }


}
