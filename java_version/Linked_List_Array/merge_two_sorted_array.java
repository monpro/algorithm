package Linked_List_Array;

import com.sun.scenario.effect.Merge;

public class merge_two_sorted_array {
    public int[] mergeSortedArray(int[] A, int[] B) {
        // write your code here
        /*
        Merge two given sorted integer array A and B into a new sorted integer array.
        A=[1,2,3,4]
        B=[2,4,5,6]
        return [1,2,2,3,4,4,5,6]
        */
        int[] result = new int[A.length + B.length];
        int left = 0, right = 0,count = 0;
        while (left < A.length && right < B.length){
            if(A[left] < B[right]){
                result[count] = A[left];
                left += 1;
            }
            else{
                result[count] = B[right];
                right += 1;
            }
            count += 1;
        }
        while (left < A.length){
            result[count] = A[left];
            count += 1;
            left += 1;
        }
        while(right <  B.length){
            result[count] = B[right];
            count += 1;
            right += 1;

        }
        return result;

    }
}
