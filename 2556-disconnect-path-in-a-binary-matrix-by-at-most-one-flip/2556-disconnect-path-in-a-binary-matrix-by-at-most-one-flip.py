class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        q = {(0, 0)}
        isReached = False
        while q:
            newQ = set()
            if len(q) == 1 and max(q) != (0, 0) and max(q) != (m - 1, n - 1):
                return True
            for i, j in q:
                if i == m - 1 and j == n - 1:
                    isReached = True
                    break
                if j < n - 1 and grid[i][j + 1]: 
                    newQ.add((i, j + 1))
                if i < m - 1 and grid[i + 1][j]:
                    newQ.add((i + 1, j))
            q = newQ
        return not isReached