class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def check(r: int, c: int) -> bool:
            up = r - len(word) >= -1
            down = r + len(word) <= m
            left = c - len(word) >= -1
            right = c + len(word) <= n
            if (r - len(word) > -1 and board[r - len(word)][c] != '#') or (r + 1 < m and board[r + 1][c] != '#'):
                up = False
            if (r + len(word) < m and board[r + len(word)][c] != '#') or (r - 1 > -1 and board[r - 1][c] != '#'):
                down = False
            if (c - len(word) > -1 and board[r][c - len(word)] != '#') or (c + 1 < n and board[r][c + 1] != '#'):
                left = False
            if (c + len(word) < n and board[r][c + len(word)] != '#') or (c - 1 > -1 and board[r][c - 1] != '#'):
                right = False
            for i in range(len(word)):
                if not (up or down or left or right):
                    break
                if up and board[r - i][c] not in [word[i], " "]:
                    up = False
                if down and board[r + i][c] not in [word[i], " "]:
                    down = False
                if left and board[r][c - i] not in [word[i], " "]:
                    left = False
                if right and board[r][c + i] not in [word[i], " "]:
                    right = False
            return up or down or left or right

        for i in range(m):
            for j in range(n):
                if board[i][j] in [word[0], " "] and check(i, j):
                    return True
        return False