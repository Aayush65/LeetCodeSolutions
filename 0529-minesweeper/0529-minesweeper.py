class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        
        # @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or i == m or j < 0 or j == n:
                return 0
            if board[i][j] == 'M':
                board[i][j] = 'X'
                return 1
            
            bombs = 0
            neighbors = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1), (i + 1, j + 1), (i + 1, j - 1), (i - 1, j + 1), (i - 1, j - 1)]
            for i1, j1 in neighbors:
                if i1 < 0 or i1 == m or j1 < 0 or j1 == n:
                    continue
                bombs += 1 if board[i1][j1] == 'M' else 0
            if bombs:
                board[i][j] = str(bombs)
                return 0
            
            board[i][j] = 'B'
            for i1, j1 in neighbors:
                if i1 < 0 or i1 == m or j1 < 0 or j1 == n:
                    continue
                if board[i1][j1] == 'E':
                    dfs(i1, j1)
            return 0
            
        dfs(*click)
        return board