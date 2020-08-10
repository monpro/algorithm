package bfs;

import java.util.PriorityQueue;

class Point implements Comparable<Point> {
    int x, y, distance;
    String dir;
    public Point(int x, int y, int distance, String dir) {
        this.x = x;
        this.y = y;
        this.distance = distance;
        this.dir = dir;
    }
    public int compareTo(Point p2) {
        if(distance == p2.distance) {
            return dir.compareTo(p2.dir);
        }
        else {
            return distance - p2.distance;
        }
    }
}

class Solution {
    public String findShortestWay(int[][] maze, int[] ball, int[] hole) {
        PriorityQueue<Point> pq = new PriorityQueue<Point>();
        int m = maze.length, n = maze[0].length;
        int[][] directions = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        String[] dirs = new String[]{"u", "d", "l", "r"};
        Point[][] points = new Point[m][n];
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++) {
                points[i][j] = new Point(i, j, Integer.MAX_VALUE, "");
            }
        }
        pq.add(new Point(ball[0], ball[1], 0, ""));
        while(!pq.isEmpty()) {
            Point point = pq.poll();
            if(points[point.x][point.y].compareTo(point) <= 0){
                continue;
            }
            points[point.x][point.y] = point;
            for(int i = 0; i < 4; i++) {
                int x = point.x, y = point.y, distance = point.distance;
                while(x >= 0 && x < m && y >= 0 && y < n && maze[x][y] == 0 && (x != hole[0] || y != hole[1])) {
                    x += directions[i][0];
                    y += directions[i][1];
                    distance += 1;
                }
                if(x != hole[0] || y != hole[1]) {
                    x -= directions[i][0];
                    y -= directions[i][1];
                    distance -= 1;
                }
                pq.add(new Point(x, y, distance, point.dir + dirs[i]));
            }
        }
        
        Point holePoint = points[hole[0]][hole[1]];
        return holePoint.distance == Integer.MAX_VALUE ? "impossible": holePoint.dir;
    }
}