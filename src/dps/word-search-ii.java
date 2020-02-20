package dps;

class TrieNode {
    TrieNode[] next = new TrieNode[26];
    String word;
}

class Solution {
    public TrieNode buildTrie(String[] words){
        TrieNode root = new TrieNode();
        for(String word: words){
            TrieNode node = root;
            for(char c : word.toCharArray()){
                int i = c - 'a';
                if(node.next[i] == null)
                    node.next[i] = new TrieNode();
                node = node.next[i];
            }
            node.word = word;
        }
        
        return root;
    }
    
    public List<String> findWords(char[][] board, String[] words) {
        List<String> result = new ArrayList<>();
        TrieNode root = buildTrie(words);
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                dfs(board, i, j, root, result);
            }
        }
        
        return result;
    }
    
    public void dfs(char[][] board, int i, int j, TrieNode node, List<String> result){
        char c = board[i][j];
        if(c == '&' || node.next[c - 'a'] == null)
            return;
        node = node.next[c - 'a'];
        if(node.word != null){
            result.add(node.word);
            node.word = null;
        }
        board[i][j] = '&';
        
        if(i > 0)
            dfs(board, i - 1, j, node, result);
        if(j > 0)
            dfs(board, i, j - 1, node, result);
        if(i < board.length - 1)
            dfs(board, i + 1, j, node, result);
        if(j < board[0].length - 1)
            dfs(board, i, j + 1, node, result);
        board[i][j] = c;
            
    }
    
}