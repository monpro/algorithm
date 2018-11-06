package netEase;

import java.util.Scanner;

public class airplot {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String string = scanner.nextLine();
        int number = getInts(string)[0];
        int max = 0;
        for(int i = 0; i <= Math.sqrt(number);i++){
            if(i + i * i <= number){
                max = i;
            }
        }
        System.out.println(max);

    }
    private static int[] getInts(String str) {
        String[] strings = str.split(" ");
        int[] ints = new int[strings.length];
        for(int i = 0; i < strings.length; i++){
            ints[i] = Integer.parseInt(strings[i]);
        }
        return ints;
    }
}
