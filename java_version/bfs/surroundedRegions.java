class UnionFind{

    int[] father;

    UnionFind(int n){
        father = new int[n];
        for (int i = 1; i < n; i++){
            father[i] = i;
        }
    }

    int find(int a){
        if (a == father[a]){
            return a;
        }
        return father[a] = find(father[a]);
    }

    void connect(int a, int b){
        int fa = find(a);
        int fb = find(b);
        if (fa != fb){
            father[Math.min(fa, fb)] = Math.max(fa, fb);
        }
    }
}

public class surroundedRegions {
    /*
     * @param board: board a 2D board containing 'X' and 'O'
     * @return: nothing
     */
    public void surroundedRegions(char[][] board) {
        // write your code here
        if (board == null || board.length == 0 || board[0].length == 0){
            return;
        }
        int n = board.length;
        int m = board[0].length;

        int total = n * m;
        UnionFind uf = new UnionFind(total + 1);
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                // check only edge 0
                if (board[i][j] == 'X'){
                    continue;
                }
                if (i == 0 || i == n - 1 || j == 0 || j == m - 1){
                    uf.connect(i * m + j, total);
                } else {
                    for (int k = 0; k < 4; k++){
                        int ni = i + dx[k];
                        int nj = j + dy[k];
                        if (board[ni][nj] == 'O'){
                            uf.connect(i * m + j, ni * m + nj);
                        }
                    }
                }
            }
        }
        for (int i = 1; i < n - 1; i++){
            for (int j = 1; j < m - 1; j++){
                if (board[i][j] == 'O' && uf.find(i * m + j) != total){
                    board[i][j] = 'X';
                }
            }
        }
    }
}
