package arrays;

class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int steps = 0;
        int n = points.length;
        for(int i = 0; i < n - 1; i++){
            int x = Math.abs(points[i + 1][0] - points[i][0]);
            int y = Math.abs(points[i + 1][1] - points[i][1]);
            
            steps += Math.max(x, y);
        }
        
        return steps;
    }
}