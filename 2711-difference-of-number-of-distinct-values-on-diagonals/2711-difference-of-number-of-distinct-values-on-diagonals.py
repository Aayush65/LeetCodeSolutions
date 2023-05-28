class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # Calculating val
                #top left
                tl = set()
                for k in range(1, i + 1):
                    if j - k >= 0:
                        tl.add(grid[i - k][j - k])
                br = set()
                for k in range(1, m - i):
                    if j + k < n:
                        br.add(grid[i + k][j + k])
                res[i][j] = abs(len(tl) - len(br))
        return res