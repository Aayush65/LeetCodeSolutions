class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def calcHour(row: int, col: int) -> int:
            return grid[row][col] + grid[row][col + 1] + grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]
        
        
        m = len(grid)
        n = len(grid[0])
        maxHours = 0
        for i in range(m - 2):
            for j in range(n - 2):
                maxHours = max(maxHours, calcHour(i, j))
        return maxHours