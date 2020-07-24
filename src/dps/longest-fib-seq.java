package dps;

class Solution {
    /*
    public int lenLongestFibSubseq(int[] A) {
        Set<Integer> set = new HashSet<>();
        for(int num: A){
            set.add(num);
        }
        int res = 2;
        for(int i = 0; i < A.length; i++){
            for(int j = i + 1; j < A.length; j++){
                int a = A[i], b = A[j], temp = 2;
                
                while(set.contains(a + b)){
                    b = a + b;
                    a = b - a;
                    temp += 1;
                }
                
                res = Math.max(res, temp);
            }
        }
        
        return res > 2 ? res: 0;
    }
    */
    /*
    public int lenLongestFibSubseq(int[] A) {
        int res = 0;
        int[][] dp = new int[A.length][A.length];
        Map<Integer, Integer> map = new HashMap<>();
        for(int j = 0; j < A.length; j++){
            map.put(A[j], j);
            for(int i = 0; i < j; i++){
                int index = map.getOrDefault(A[j] - A[i], -1);
                dp[i][j] = (A[j] - A[i] < A[i] && index != -1) ? dp[index][i] + 1: 2;
                res = Math.max(dp[i][j], res);
            }
        }
        return res > 2 ? res: 0;
    }
    */
    public int lenLongestFibSubseq(int[] A) {
        int n = A.length;
        int max = 0;
        int[][] dp = new int[n][n];
        for(int i = 0; i < dp.length; i++){
            for(int j = 0; j < dp[0].length; j++){
                dp[i][j] = 2;
            }
        }
        for (int i = 2; i < n; i++) {
            int l = 0, r = i - 1;
	        while (l < r) {
                int sum = A[l] + A[r];
                if (sum > A[i]) {
                    r--;  
                } else if (sum < A[i]) {
                    l++;
                } else {
                    dp[r][i] = dp[l][r] + 1;
                    max = Math.max(max, dp[r][i]);
                    r--;
                    l++;
                }
            }
        }
        return max == 2 ? 0 : max;
    }
    
}