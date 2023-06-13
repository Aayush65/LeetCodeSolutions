class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowMap = defaultdict(int)
        for i in grid:
            rowMap[tuple(i)] += 1
        
        colMap = defaultdict(int)
        colSet = set()
        for i in range(len(grid)):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            col = tuple(col)
            colMap[col] += 1
            colSet.add(col)
            
        commons = 0
        for i in colSet:
            commons += colMap[i] * rowMap[i]
        return commons