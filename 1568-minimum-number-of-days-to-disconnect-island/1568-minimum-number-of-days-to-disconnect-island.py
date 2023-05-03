class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i: int, j: int, val: int, toCheck: int) -> None:
            if i == m or i == -1 or j == n or j == -1 or grid[i][j] != toCheck:
                return
            grid[i][j] = val
            dfs(i + 1, j, val, toCheck)
            dfs(i, j + 1, val, toCheck)
            dfs(i - 1, j, val, toCheck)
            dfs(i, j - 1, val, toCheck)

        lands = 0
        islandFound = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if islandFound:
                        return 0
                    dfs(i, j, 3, 1)
                    islandFound = True
                if grid[i][j]:
                    lands += 1

        if lands < 3:
            return lands

        def noOfIslands(val: int) -> int:
            islands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == val:
                        dfs(i, j, val + 1, val)
                        islands += 1
            return islands

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    val = grid[i][j]
                    grid[i][j] = 0
                    if noOfIslands(val) > 1:
                        return 1
                    grid[i][j] = val + 1
        return 2