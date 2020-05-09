class Solution {
    public int maximumSwap(int num) {
        char[] array = Integer.toString(num).toCharArray();
        int[] pos = new int[10];
        for(int i = 0; i < array.length; i++){
            pos[array[i] - '0'] = i;
        }
        
        for(int i = 0; i < array.length; i++){
            for(int j = 9; j > array[i] - '0'; j--){
                if(pos[j] > i){
                    swap(array, i, pos[j]);
                    return Integer.valueOf(new String(array));
                }
            }
        }
        return num;
    }
    
    public void swap(char[] array, int i, int j){
        char temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}