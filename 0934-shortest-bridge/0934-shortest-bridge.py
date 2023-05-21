class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])        
        
        def dfs(i: int, j: int, val: int):
            if -1 < i < m and -1 < j < n and grid[i][j] == 1:
                boundary.append((i, j))
                grid[i][j] = val
                dfs(i, j + 1, val)
                dfs(i + 1, j, val)
                dfs(i, j - 1, val)
                dfs(i - 1, j, val)
            
        island = 2
        boundary = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, island)
                    island += 1
                    break
            if boundary: break
        
        q = set(boundary)
        bridge = -1
        visited = set()
        while True:
            nextQ = set()
            for i, j in q:
                if i < 0 or i == m or j < 0 or j == n or (i, j) in visited:
                    continue
                visited.add((i, j))
                if grid[i][j] == 1:
                    return bridge
                nextQ.add((i, j + 1))
                nextQ.add((i + 1, j))
                nextQ.add((i, j - 1))
                nextQ.add((i - 1, j))
            bridge += 1
            q = nextQ