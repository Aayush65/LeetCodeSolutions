class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = int(1e9 + 7)
        m = len(grid)
        n = len(grid[0])
        
        isValid = lambda x, y: -1 < x < m and -1 < y < n
        
        @cache
        def dfs(i: int, j: int) -> int:
            res = 1
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if isValid(x, y) and grid[x][y] > grid[i][j]:
                    res += dfs(x, y)
            return res % MOD
            
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (ans + dfs(i, j)) % MOD
        return ans