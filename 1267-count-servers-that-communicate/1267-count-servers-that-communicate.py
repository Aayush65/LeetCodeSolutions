class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rowSum = []
        for i in range(m):
            total = 0
            one = -1
            for j in range(n):
                total += grid[i][j]
                if grid[i][j]:
                    one = j
            rowSum.append([total, one])
                
        colSum = []
        for i in range(n):
            total = 0
            for j in range(m):
                total += grid[j][i]
            colSum.append(total)
        
        servers = 0
        for i, c in rowSum:
            if i > 1:
                servers += i
            else:
                if i and colSum[c] > 1:
                    servers += 1
        return servers