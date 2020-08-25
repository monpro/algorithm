package dps;

import java.util.Arrays;

class Solution {
    public int minDifficulty(int[] jobDifficulty, int d) {
        int n = jobDifficulty.length;
        if (n < d) return -1;
        // the minimum difficulty from 0..i in days d
        int[][] cache = new int[n][d+1];
        for (int i = 0; i < n; i++) {Arrays.fill(cache[i], -1);}
        return dfs(jobDifficulty, 0, d, cache);
    }

    private int dfs(int[] arr, int i, int d, int[][] cache) {
        if (cache[i][d] != -1) return cache[i][d];
        int n = arr.length;
        if (d == 1) {
            int max = 0;
            while (i < n) max = Math.max(max, arr[i++]);
            return max;
        }
        int res = Integer.MAX_VALUE, maxDifficulty = 0;
        for (int j = i; j < n - d + 1; j++) {
            maxDifficulty = Math.max(arr[j], maxDifficulty);
            res = Math.min(res, maxDifficulty + dfs(arr, j + 1, d - 1, cache));
        }
        return cache[i][d] = res;
    }
}