class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        dp = dungeon.copy()
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i, j) == (m - 1, n - 1):
                    dp[i][j] = min(0, dp[i][j])
                    continue
                down = dp[i + 1][j] if i < m - 1 else -float("inf")
                right = dp[i][j + 1] if j < n - 1 else -float("inf")
                dp[i][j] = min(0, max(down, right) + dp[i][j])
        return -dp[0][0] + 1