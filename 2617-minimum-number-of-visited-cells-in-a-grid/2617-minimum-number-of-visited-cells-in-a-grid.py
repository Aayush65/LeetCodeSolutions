class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = {(0, 0)}
        visited = set()
        steps = 1
        while q:
            newQ = set()
            for i, j in q:
                if (i, j) in visited:
                    continue
                if (i, j) == (m - 1, n - 1):
                    return steps
                visited.add((i, j))
                for k in range(j + 1, min(n, grid[i][j] + j + 1), 1):
                    if (i, k) == (m - 1, n - 1):
                        return steps + 1
                    newQ.add((i, k))
                for k in range(i + 1, min(m, grid[i][j] + i + 1), 1):
                    if (k, j) == (m - 1, n - 1):
                        return steps + 1
                    newQ.add((k, j))
            q = newQ
            steps += 1
        return -1