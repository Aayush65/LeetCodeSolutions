class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = int(1e9 + 7)
        n = len(board)
        board = [[int(i) if i not in {'E','X','S'} else -1 for i in j] for j in board]
        board[0][0] = 0
        board[-1][-1] = 0
        
        @cache
        def dp(r: int, c: int) -> list[int]:
            if r == n or c == n or board[r][c] == -1:
                return [-float("inf"), 0]
            if (r, c) == (n - 1, n - 1):
                return [0, 1] # 0 value and 1 way
            
            down = dp(r + 1, c)
            right = dp(r, c + 1)
            cross = dp(r + 1, c + 1)
            
            maxVal = max(down[0], right[0], cross[0])
            ways = 0
            if maxVal == down[0]:
                ways += down[1]
            if maxVal == right[0]:
                ways += right[1]
            if maxVal == cross[0]:
                ways += cross[1]
            return [maxVal + board[r][c], ways % mod]
        
        res = dp(0, 0)
        return [0, 0] if res[0] < 0 else res