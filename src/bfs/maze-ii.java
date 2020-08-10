package bfs;

import java.util.*;

class Point {
    int x, y, distance;
    public Point(int x, int y, int distance) {
        this.x = x;
        this.y = y;
        this.distance = distance;
    }
}

class Solution {
    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        PriorityQueue<Point> pq = new PriorityQueue<Point>((p1, p2) -> p1.distance - p2.distance);
        int m = maze.length, n = maze[0].length;
        int[][] directions = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int[][] dist = new int[m][n];
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++) {
                dist[i][j] = Integer.MAX_VALUE;
            }
        }
        pq.add(new Point(start[0], start[1], 0));
        
        while(!pq.isEmpty()) {
            Point point = pq.poll();
            if (point.x == destination[0] && point.y == destination[1]) {
                return point.distance;
            }
            if(point.distance >= dist[point.x][point.y]) {
                continue;
            }
            dist[point.x][point.y] = point.distance;
            
            for(int[] d: directions) {
                int x = point.x;
                int y = point.y;
                int distance = point.distance;
                
                while(x >= 0 && x < m && y >= 0 && y < n && maze[x][y] == 0) {
                    x += d[0];
                    y += d[1];
                    distance += 1;
                }
                
                x -= d[0];
                y -= d[1];
                distance -= 1;
                pq.offer(new Point(x, y, distance));
            }
        }
        
        return -1;
    }
}