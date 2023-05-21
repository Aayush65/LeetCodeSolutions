class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        memo = {}
        def dp(row: int, col: int) -> int:
            if (row, col) in memo:
                return memo[(row, col)]
            val = grid[row][col]
            if row == m - 1:
                return val
            cost = float("inf")
            for i in range(n):
                cost = min(cost, dp(row + 1, i) + moveCost[val][i])
            memo[(row, col)] = val + cost
            return val + cost
        
        return min(dp(0, i) for i in range(n))