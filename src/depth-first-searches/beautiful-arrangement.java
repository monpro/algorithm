class Solution {
    public int countArrangement(int N) {
        if(N == 0)
            return 0;
        
        int[] result = new int[1];
        int[] used = new int[N + 1];
        helper(N, 1, used, result);
        return result[0];
    }
    
    public void helper(int N, int pos, int[] used, int[] result){
        if(pos > N){
            result[0]++;
            return;
        }
        for(int i = 1; i <= N; i++){
            if(used[i] == 0 && (i % pos == 0 || pos % i == 0)){
                used[i] = 1;
                helper(N, pos + 1, used, result);
                used[i] = 0;
            }
        }
    }
}