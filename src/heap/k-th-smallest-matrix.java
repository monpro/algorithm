package heap;

import java.util.*;
class Node {
  int row;
  int col;

  public Node(int row, int col){
    this.row = row;
    this.col = col;
  }
}

class KthSmallestInSortedMatrix {

  public static int findKthSmallest(int[][] matrix, int k) {
    PriorityQueue<Node> minHeap = new PriorityQueue<>((n1, n2) -> matrix[n1.row][n1.col] - matrix[n2.row][n2.col]);
    for(int i = 0; i < matrix.length && i < k; i++){
      if(matrix[i].length > 0){
        minHeap.add(new Node(i, 0));
      }
    }
    int result = 0;
    int index = 0;

    while(!minHeap.isEmpty()){
      Node node = minHeap.poll();
      result = matrix[node.row][node.col];
      index += 1;
      if(index == k){
        break;
      }
      if(node.col + 1 <= matrix[node.row].length - 1){
        node.col += 1;
        minHeap.add(node);
      }
    }
    return result;
  }

  public static void main(String[] args) {
    int matrix[][] = { { 2, 6, 8 }, { 3, 7, 10 }, { 5, 8, 11 } };
    int result = KthSmallestInSortedMatrix.findKthSmallest(matrix, 5);
    System.out.print("Kth smallest number is: " + result);
  }
}