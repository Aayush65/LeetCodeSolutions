class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        isValid = lambda x, y: -1 < x < m and -1 < y < n and grid[x][y]
        def dfs(r: int, c: int) -> int:
            if isValid(r, c):
                res = grid[r][c]
                grid[r][c] = 0
                res += dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)
                return res
            return 0
        
        maxFish = 0
        for i in range(m):
            for j in range(n):
                fish = dfs(i, j)
                maxFish = max(maxFish, fish)
        return maxFish