package dps;

class TreeAncestor {
    int[][] dp;
    int maxPower;

    public TreeAncestor(int n, int[] parent) {
        this.maxPower = (int) (Math.log(n) / Math.log(2)) + 1;

        this.dp = new int[maxPower][n];
        dp[0] = parent;

        for (int i = 1; i < maxPower; i++) {
            for (int j = 0; j < n; j++) {
                int pre_ancestor = dp[i - 1][j];
                if (pre_ancestor == -1) {
                    dp[i][j] = -1;
                } else {
                    dp[i][j] = dp[i - 1][pre_ancestor];
                }
            }
        }
    }

    public int getKthAncestor(int node, int k) {
        int curPower = this.maxPower; // base 2
        while (k > 0 && node >= 0) {
            int powNum = 1 << curPower;
            if (k >= powNum) {
                node = dp[curPower][node];
                k -= powNum;
            } else {
                curPower -= 1;
            }
        }
        return node;
    }
}