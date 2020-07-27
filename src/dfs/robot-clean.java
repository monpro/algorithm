package dfs;

import java.util.*;

class Robot {
    public void clean() {
    }

    public boolean move() {
        return false;
    }

    public void turnRight() {
    }
}

class Solution {

    private static final int[][] directions = new int[][] { { 0, -1 }, { 1, 0 }, { 0, 1 }, { -1, 0 } };

    public void cleanRoom(Robot robot) {
        dfs(robot, 0, 0, 0, new HashSet<>());
    }

    public void dfs(Robot robot, int x, int y, int cur, Set<String> visited) {
        robot.clean();
        visited.add(x + "->" + y);

        for (int i = cur; i < cur + 4; i++) {
            int nextX = directions[i % 4][0] + x;
            int nextY = directions[i % 4][1] + y;

            if (!visited.contains(nextX + "->" + nextY) && robot.move()) {
                dfs(robot, nextX, nextY, i % 4, visited);
            }
            robot.turnRight();
        }
        robot.turnRight();
        robot.turnRight();
        robot.move();
        robot.turnRight();
        robot.turnRight();

    }
}