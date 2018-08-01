package bfs;

public class Main {

    public static void main(String[] args) {
        search_a_2d_matrix search_a_2d_matrix = new search_a_2d_matrix();
        int [][] array = {{1,3,5,7},{10,11,16,20},{23,30,34,50}};
        System.out.println(search_a_2d_matrix.searchMatrix(array,3));

    }
}
