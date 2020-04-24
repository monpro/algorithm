class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int[] prefix = new int[K];
        prefix[0] = 1;
        int cur = 0, result = 0;
        for(int num: A){
            cur = (cur + num) % K;
            if(cur < 0) cur += K;
            result += prefix[cur];
            prefix[cur] += 1;
        }
        
        return result;
    }
}