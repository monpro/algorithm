package Linked_List_Array;
/*
There are two sorted arrays A and B of size m and n respectively.
Find the median of the two sorted arrays.

Example
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.
Given A=[1,2,3] and B=[4,5], the median is 3.
Challenge
The overall run time complexity should be O(log (m+n))
 */
public class median_of_two_sorted_array {
    public double findMedianSortedArrays(int[] A, int[] B) {
        // write your code here
        int length = A.length + B.length;
        if(length % 2 == 0){
            return (findKthElement(A,0,B,0,length / 2)
                    + findKthElement(A,0,B,0,length / 2 + 1)
            )/2.0;
        }
        return findKthElement(A,0,B,0,length / 2 + 1);
    }

    int findKthElement(int[] A, int startA, int[] B, int startB, int k){
        if(startA >=  A.length){
            return B[startB + k - 1];
        }
        if(startB >= B.length){
            return A[startA + k - 1];
        }

        if(k == 1){
            return Math.min(A[startA], B[startB]);
        }
        int halfKthOfA = Integer.MAX_VALUE;
        int halfKthOfB = Integer.MAX_VALUE;
        if(startA + k / 2 - 1 < A.length){
             halfKthOfA = A[startA + k / 2 - 1];
        }
        if(startB + k / 2 - 1 < B.length){
            halfKthOfB = B[startB + k / 2 - 1];
        }

        if(halfKthOfA < halfKthOfB){
            return findKthElement(A,startA + k / 2, B, startB, k - k / 2);
        }else{
            return findKthElement(A,startA,B,startB + k / 2, k - k / 2);
        }
    }

}
