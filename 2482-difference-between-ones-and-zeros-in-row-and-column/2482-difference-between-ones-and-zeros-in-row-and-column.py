class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = []
        onesCol = []
        M = len(grid)
        N = len(grid[0])
        for i in range(M):
            row = 0
            for j in range(N):
                if grid[i][j] == 1:
                    row += 1
            onesRow.append(row)
        for i in range(N):
            col = 0
            for j in range(M):
                if grid[j][i] == 1:
                    col += 1
            onesCol.append(col)
        
        diff = []
        for i in range(M):
            diffRow = []
            for j in range(N):
                diffRow.append((onesRow[i] + onesCol[j])*2 - M - N)
            diff.append(diffRow)
        return diff