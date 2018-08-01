package netEase;

import java.util.Scanner;

public class move_apple {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String str2 = sc.nextLine();
        int cow_number = getInts(str)[0];
        int[] cow_apple = getInts(str2);
        int sum = 0;
        for(Integer apple: cow_apple){
            sum += apple;
        }
        if(sum % cow_number != 0){
            System.out.println(-1);
        }
        else {
            int average = sum / cow_number;
            int result = 0;
            for(Integer i: cow_apple){
                if((average - i) % 2 != 0 || (i - average) % 2 != 0 ){
                    System.out.println(-1);
                    return;
                }
                if(i < average){
                    result += (int)Math.ceil((average - i) / 2);

                }
            }
            System.out.println(result);

        }


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
