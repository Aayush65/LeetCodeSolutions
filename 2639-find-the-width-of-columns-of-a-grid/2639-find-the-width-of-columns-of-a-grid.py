class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        res = [0] * n
        for i in range(n):
            for j in range(m):
                res[i] = max(res[i], len(str(grid[j][i])))
        return res