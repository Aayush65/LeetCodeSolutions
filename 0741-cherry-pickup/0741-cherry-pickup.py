class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        isValid = lambda x, y: 0 <= x < n and 0 <= y < n and grid[x][y] != -1
        memo = {}

        def dfs(i1: int, j1: int, i2: int, j2: int) -> int:
            if (i1, i2, j1, j2) in memo:
                return memo[(i1, i2, j1, j2)]
            if not isValid(i1, j1) or not isValid(i2, j2):
                return -float("inf")
            if i1 + j1 + i2 + j2 == 4 * (n - 1):
                return grid[i1][j1]
            currVal = grid[i1][j1] if (i1, j1) == (i2, j2) else grid[i1][j1] + grid[i2][j2]
            rr = dfs(i1, j1 + 1, i2, j2 + 1)
            rd = dfs(i1, j1 + 1, i2 + 1, j2)
            dr = dfs(i1 + 1, j1, i2, j2 + 1)
            dd = dfs(i1 + 1, j1, i2 + 1, j2)
            res = currVal + max(rr, rd, dr, dd)
            memo[(i1, i2, j1, j2)] = res
            return res

        return max(0, dfs(0, 0, 0, 0))