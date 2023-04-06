class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        isValid = lambda i, j: -1 < i < m and -1 < j < n
        
        def changeByDFS(r: int, c: int) -> None:
            if isValid(r, c) and not grid[r][c]:
                grid[r][c] = 1
                changeByDFS(r + 1, c)
                changeByDFS(r, c + 1)
                changeByDFS(r - 1, c)                
                changeByDFS(r, c - 1)
        
        for i in range(m):
            changeByDFS(i, 0)
            changeByDFS(i, n - 1)
        for i in range(n):
            changeByDFS(0, i)
            changeByDFS(m - 1, i)
            
        isLands = 0
        for i in range(1, m):
            for j in range(1, n):
                if not grid[i][j]:
                    isLands += 1
                    changeByDFS(i, j)
        return isLands