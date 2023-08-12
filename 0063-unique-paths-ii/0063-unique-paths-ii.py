class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        dp = [[0 for i in range(N)] for j in range(M)]
        dp[0][0] = 0 if grid[0][0] else 1

        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    continue
                dp[i][j] += dp[i - 1][j] if i > 0 else 0
                dp[i][j] += dp[i][j - 1] if j > 0 else 0
        
        return dp[-1][-1]