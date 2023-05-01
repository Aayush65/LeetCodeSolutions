class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        tictactoe = ''.join(board)
        x = o = 0
        for i in tictactoe:
            if i == 'X':
                x += 1
            if i == 'O':
                o += 1
                
        XWins = OWins = False
        if {board[0][0], board[1][1], board[2][2]} == {'X'}:
            XWins = True
        if {board[0][2], board[1][1], board[2][0]} == {'X'}:
            XWins = True
        if {board[0][0], board[1][1], board[2][2]} == {'O'}:
            OWins = True
        if {board[0][2], board[1][1], board[2][0]} == {'O'}:
            OWins = True
        
        for i in range(3):
            if {board[i][0], board[i][1], board[i][2]} == {'X'}:
                XWins = True
            if {board[0][i], board[1][i], board[2][i]} == {'X'}:
                XWins = True
        for i in range(3):
            if {board[i][0], board[i][1], board[i][2]} == {'O'}:
                OWins = True
            if {board[0][i], board[1][i], board[2][i]} == {'O'}:
                OWins = True
                
        if XWins and OWins:
            return False
        if XWins:
            return x == o + 1
        if OWins:
            return x == o
        
        if o > x:
            return False
        return x == o or x == o + 1