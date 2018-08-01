package Linked_List_Array;

/*
Given two sorted integer arrays A and B, merge B into A as one sorted array.
Example
A = [1, 2, 3, empty, empty], B = [4, 5]
After merge, A will be filled as [1, 2, 3, 4, 5]
You may assume that A has enough space (size that is greater or equal to m + n)
to hold additional elements from B. The number of elements initialized in A and B
are m and n respectively.
 */
public class merge_sorted_array {
    public void mergeSortedArray(int[] A, int m, int[] B, int n) {
        int i = m - 1, j = n - 1, index = m + n - 1;
        while (i >= 0 && j >= 0){
            if(A[i] > B[j]){
                A[index] = A[i];
                index -= 1;
                i -= 1;
            }
            else{
                A[index] = B[j];
                index -= 1;
                j -= 1;
            }
        }
        while (i >= 0){
            A[index] = A[i];
            index -= 1;
            i -= 1;
        }
        while (j >= 0){
            A[index] = B[j];
            j -= 1;
            index -= 1;
        }
    }
}
