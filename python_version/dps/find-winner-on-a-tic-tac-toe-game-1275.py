class Solution:
    def tictactoe(self, moves):
        if len(moves) == 0 or len(moves[0]) == 0:
            return 'Draw'
        # 0 - 2 for each row
        # 3 - 5 for each column
        # 6 - 7 for dignoal    
        score = [[0] * 8 for _ in range(2)]
        player = 0
        for i, j in moves:
            score[player][i] += 1
            score[player][3 + j] += 1
            score[player][6] += i == j
            score[player][7] += i + j == 2
            if 3 in (score[player][i], score[player][3 + j], score[player][6], score[player][7]):
                return "AB"[player]
            player ^= 1
        
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
        