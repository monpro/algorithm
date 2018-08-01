package dfs;

import java.util.ArrayList;
import java.util.List;

public class N_Queens {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> results = new ArrayList<>();
        if (n == 0) {
            return results;
        }
        //queen could attack down, left down, right down
        helper(results, new ArrayList<>(), n);
        return results;
    }


    void helper(List<List<String>> results, List<Integer> subset, int n) {
        if (subset.size() == n) {
            results.add(draw_chess_board(subset));
            return;
        }

        for (int index = 0; index < n; index++) {
            if (!isValid(index, subset)) {
                continue;
            }
            subset.add(index);
            helper(results, new ArrayList<>(subset), n);
            subset.remove(subset.size() - 1);

        }
    }

    List<String> draw_chess_board(List<Integer> subset){
        List<String> resuslt = new ArrayList<>();
        int number = subset.size();
        for(Integer integer: subset){
            StringBuilder stringBuilder = new StringBuilder();
            for(int i = 0; i < number; i++){
                if(i!= integer){
                    stringBuilder.append(".");
                }
                else{
                    stringBuilder.append('Q');
                }
            }
            resuslt.add(stringBuilder.toString());
        }
        return resuslt;



    }
    boolean isValid(int index, List<Integer> subset) {
        //how to judge whether it is Valid
        //...0   ..0.  ..0.
        //..0.   ...0  ..0.
        int row = subset.size();
        for (int rowIndex = 0; rowIndex < row; rowIndex++) {
            if (subset.get(rowIndex) == index) {
                return false;
            }
            if(subset.get(rowIndex) + rowIndex == row + index){
                return false;
            }

            if(subset.get(rowIndex) - rowIndex == index - row){
                return false;
            }
        }
        return true;
    }
}
