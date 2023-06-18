class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        # @cache
        memo = [[-1] * n for i in range(m)]
        def dfs(i: int, j: int) -> int:
            if memo[i][j] != -1:
                return memo[i][j]
            steps = 0

            rowStart = bisect_left(rows[i], mat[i][j] + 1, key = lambda x: x[0])
            for colIdx in range(rowStart, n):
                if rows[i][colIdx][0] != rows[i][rowStart][0]:
                    break
                steps = max(steps, dfs(i, rows[i][colIdx][1]))

            colStart = bisect_left(cols[j], mat[i][j] + 1, key = lambda x: x[0])
            for rowIdx in range(colStart, m):
                if cols[j][rowIdx][0] != cols[j][colStart][0]:
                    break
                steps = max(steps, dfs(cols[j][rowIdx][1], j))

            memo[i][j] = 1 + steps
            return 1 + steps
    

        rows = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append((mat[i][j], j))
            rows.append(sorted(row))

        cols = []
        for i in range(n):
            col = []
            for j in range(m):
                col.append((mat[j][i], j))
            cols.append(sorted(col))

        maxSteps = 0
        for i in range(m):
            for j in range(n):
                maxSteps = max(maxSteps, dfs(i, j))
        return maxSteps