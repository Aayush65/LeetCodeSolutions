class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
    
        q = [(grid[0][0], 0, 0)]
        visited = set()
        while q:
            time, i, j = heappop(q)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if (i, j) == (n - 1, n - 1):
                return time
            
            if i > 0:
                heappush(q, (max(time, grid[i - 1][j]), i - 1, j))
            if j > 0:
                heappush(q, (max(time, grid[i][j - 1]), i, j - 1))
            if i < n - 1:
                heappush(q, (max(time, grid[i + 1][j]), i + 1, j))
            if j < n - 1:
                heappush(q, (max(time, grid[i][j + 1]), i, j + 1))
