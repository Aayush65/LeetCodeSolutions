import pprint
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = int(1e9 + 7)
        m = len(grid)
        n = len(grid[0])
        dp = [[[] for j in range(n)] for i in range(m)]
        dp[-1][-1] = [grid[-1][-1], grid[-1][-1]]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i, j) == (m - 1, n - 1): continue
                allVals = set()
                if i < m - 1:
                    allVals.add(dp[i + 1][j][0])
                    allVals.add(dp[i + 1][j][1])
                if j < n - 1:
                    allVals.add(dp[i][j + 1][0])
                    allVals.add(dp[i][j + 1][1])
                allVals = [k * grid[i][j] for k in allVals]
                dp[i][j] = [max(allVals), min(allVals)]

        return dp[0][0][0] % mod if dp[0][0][0] > -1 else -1