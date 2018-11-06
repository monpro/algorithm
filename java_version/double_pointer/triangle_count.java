package double_pointer;

import java.util.Arrays;
import java.util.Scanner;

/*
Given an array of integers,
how many three numbers can be found in the array,
 so that we can build an triangle whose three edges
 length is the three numbers that we find?
Example
Given array S = [3,4,6,7], return 3. They are:
[3,4,6]
[3,6,7]
[4,6,7]

Given array S = [4,4,4,4], return 4. They are:

[4(1),4(2),4(3)]
[4(1),4(2),4(4)]
[4(1),4(3),4(4)]
[4(2),4(3),4(4)]
 */
public class triangle_count {
    public static int triangleCount(int[] S) {
        // write your code here
        if(S.length == 0){
            return 0;
        }
        Arrays.sort(S);
        int result = 0;
        //when to build triangle edge1 + edge2 > edge3 && Math.abs(edge1 - edge2) < edge3
        int left = 0, right = S.length - 1;
        for(int i = 0; i < S.length;i++){
            left = 0;
            right = i - 1;
            while (left < right){
                //S[i] is the max edge
                if(S[left] + S[right] > S[i]){
                    result += right - left;
                    right -= 1;
                }
                else{
                    left += 1;
                }
            }
        }
        return result;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String str_2 = sc.nextLine();
        String str_3 = sc.nextLine();
        int[] ints = getInts(str);
        int[] ints1 = getInts(str_2);
        int[] ints2 = getInts(str_3);
        for(Integer i : ints){
            System.out.println(i);
        }
        System.out.println("************");
        for(Integer i : ints1){
            System.out.println(i);
        }
        System.out.println("************");

        for(Integer i: ints2){
            System.out.println(i);
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
