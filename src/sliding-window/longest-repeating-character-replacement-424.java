class Solution {
    public int characterReplacement(String s, int k) {
        char[] scArray = s.toCharArray();
        int[] count = new int[26];
        int maxCount = 0, start = 0, result = 0;
        for(int i = 0; i < scArray.length; i++){
            int index = scArray[i] - 'A';
            count[index] += 1;
            maxCount = Math.max(maxCount, count[index]);
            if(maxCount + k < i - start + 1){
                int startIndex = scArray[start] - 'A';
                count[startIndex] -= 1;
                start += 1;
            }
            
            result = Math.max(result, i - start + 1);
        }
        return result;
    }
}