class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowMax = [max(i) for i in grid]
        colMax = []
        for i in range(n):
            maxi = 0
            for j in range(n):
                maxi = max(maxi, grid[j][i])
            colMax.append(maxi)
            
        increase = 0
        for i in range(n):
            for j in range(n):
                increase += max(grid[i][j], min(rowMax[i], colMax[j])) - grid[i][j]
        return increase