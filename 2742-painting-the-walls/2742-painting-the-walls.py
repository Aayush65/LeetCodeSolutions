class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(n):
            for walls in range(n, 0, -1):
                dp[walls] = min(dp[walls], dp[max(walls - time[i] - 1, 0)] + cost[i])

        return dp[n]
