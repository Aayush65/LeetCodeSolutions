class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = {(m-1, n-1): grid[m-1][n-1]}

        def weightedGrid(i: int, j: int) -> int:
            if i >= m or j >= n:
                return float("inf")
            if (i, j) in memo:
                return memo[(i, j)]
            weight = grid[i][j] + min(weightedGrid(i + 1, j), weightedGrid(i, j + 1))
            memo[(i, j)] = weight
            return weight
        
        return weightedGrid(0, 0)