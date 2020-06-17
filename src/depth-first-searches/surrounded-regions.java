class Solution {
    public void solve(char[][] board) {
        if(board.length == 0 || board[0].length == 0)
            return;
        
        int row = board.length, col = board[0].length;
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if((i == 0 || i == row - 1 || j == 0 || j == col - 1) && board[i][j] == 'O'){
                    dfs(board, i, j);
                }
                    
            }
        }
        
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(board[i][j] == 'O')
                    board[i][j] = 'X';
                else if(board[i][j] == 'M')
                    board[i][j] = 'O';
            }
        }
        
        return;
    }
    
    public void dfs(char[][] board, int i, int j){
        if(i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] == 'X' || board[i][j] == 'M')
            return;
        board[i][j] = 'M';
        
        dfs(board, i + 1, j);
        dfs(board, i - 1, j);
        dfs(board, i, j + 1);
        dfs(board, i, j - 1);
    }
}