class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        mod = 12345
        
        findIdx = lambda x, y: x * m + y
        preMul = []
        curr = 1
        for i in grid:
            for j in i:
                curr *= j
                curr %= mod
                preMul.append(curr)
        
        grid.reverse()
        suffMul = []
        curr = 1
        for i in grid:
            i.reverse()
            for j in i:
                curr *= j
                curr %= mod
                suffMul.append(curr)
        suffMul.reverse()
        
        res = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                index = findIdx(i, j)
                left = right = 1
                if index > 0:
                    left = preMul[index - 1]
                if index < m * n - 1:
                    right = suffMul[index + 1]
                res[i][j] = (left * right) % mod
        return res