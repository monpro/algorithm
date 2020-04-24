class Solution {
    public boolean canCross(int[] stones) {
        boolean[][] dps = new boolean[1111][1111];
        int N = stones.length;
        dps[0][0] = true;
        for(int i = 1; i < N;i++){
            for(int j = 0; j < i; j++){
                int diff = stones[i] - stones[j];
                if(diff >= 1110 || diff < 0)
                    continue;
                
                if(dps[j][diff] || dps[j][diff + 1] || dps[j][diff - 1])
                    dps[i][diff] = true;
                
            }
        }
        
        for(int i = 0; i < N; i++){
            if(dps[N - 1][i] == true)
                return true;
        }
        return false;
    }
}