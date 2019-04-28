package tree;

import java.util.Arrays;

public class Main {
    public static void main(String[] args){
        int[] array = new int[]{2,3,4,5,6};
        int[] sub = Arrays.copyOfRange(array,0,array.length);
        for(int i = 0; i < sub.length; i++){
            System.out.println(sub[i]);
        }
    }
}
