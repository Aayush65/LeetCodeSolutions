class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = {(i, 0) for i in range(m)}
        
        steps = 0
        while q:
            newQ = set()
            for i, j in q:
                if i > 0 and j < n - 1 and grid[i - 1][j + 1] > grid[i][j]:
                    newQ.add((i - 1, j + 1))
                if j < n - 1 and grid[i][j + 1] > grid[i][j]:
                    newQ.add((i, j + 1))
                if i < m - 1 and j < n - 1 and grid[i + 1][j + 1] > grid[i][j]:
                    newQ.add((i + 1, j + 1))
            steps += 1
            q = newQ
        return steps - 1