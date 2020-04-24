class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """

    def exist(self, board, word):
        if len(word) == 0:
            return False
        if len(board) == 0 or len(board[0]) == 0:
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if self.helper(board, word, i, j, 0):
                        return True
        return False

    def helper(self, board, word, row, col, index):
        if index == len(word):
            return True
        if row == len(board) or col == len(board[0]) or row < 0 or col < 0 or board[row][col] != word[index]:
            return False

        board[row][col] = "-1"
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        result = False
        for direction in directions:
            if self.helper(board, word, row + direction[0], col + direction[1], index + 1):
                return True
        board[row][col] = word[index]
        return result
