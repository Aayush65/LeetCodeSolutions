class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        isValid = lambda i, j: -1 < i < m and -1 < j < n
        
        def changeByDFS(r: int, c: int) -> int:
            res = 0
            if isValid(r, c) and grid[r][c]:
                grid[r][c] = 0
                res += 1
                res += changeByDFS(r + 1, c)
                res += changeByDFS(r, c + 1)
                res += changeByDFS(r - 1, c)                
                res += changeByDFS(r, c - 1)
            return res
        
        for i in range(m):
            changeByDFS(i, 0)
            changeByDFS(i, n - 1)
        for i in range(n):
            changeByDFS(0, i)
            changeByDFS(m - 1, i)
            
        isLands = 0
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j]:
                    isLands += changeByDFS(i, j)
        return isLands