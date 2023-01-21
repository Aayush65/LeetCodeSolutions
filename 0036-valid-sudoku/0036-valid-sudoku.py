class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rSet = set()
            cSet = set()
            bSet = set()
            for j in range(9):
                if board[i][j] != '.':
                    if int(board[i][j]) < 10 and board[i][j] not in rSet:
                        rSet.add(board[i][j])
                    else:
                        return False
                if board[j][i] != '.':
                    if int(board[j][i]) < 10 and board[j][i] not in cSet:
                        cSet.add(board[j][i])
                    else:
                        return False
                boxI = (i // 3) * 3 + j // 3
                boxJ = (i % 3) * 3 + j % 3
                if board[boxI][boxJ] != '.':
                    if int(board[boxI][boxJ]) < 10 and board[boxI][boxJ] not in bSet:
                        bSet.add(board[boxI][boxJ])
                    else:
                        return False
        return True