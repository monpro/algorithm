class Solution {
    public int[] constructArray(int n, int k) {
        int[] result = new int[n];
        for(int i = 0; i < n; i++)
            result[i] = i + 1;
        for(int i = 0, j = 0; i <= k; j++){
            result[i++] = j + 1;
            if(i < k)
                result[i++] = k - j + 1;
        }
        return result;
    }
}