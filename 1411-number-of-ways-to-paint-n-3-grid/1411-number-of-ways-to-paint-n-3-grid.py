class Solution:
    def numOfWays(self, n: int) -> int:
        mod = int(1e9 + 7)
        m = 3
        allCols = []
        currCol = []
        
        def findAllCols(index: int) -> None:
            if index == m:
                allCols.append(currCol.copy())
                return
            for i in range(3):
                if currCol and currCol[-1] == i:
                    continue
                currCol.append(i)
                findAllCols(index + 1)
                currCol.pop()
        
        findAllCols(0)
        
        def isCompatible(c1: int, c2: int) -> bool:
            for i in range(m):
                if allCols[c1][i] == allCols[c2][i]:
                    return False
            return True
        
        canBeNext = {i: [] for i in range(len(allCols))}
        canBeNext[-1] = [i for i in range(len(allCols))]
        for i in range(len(allCols)):
            for j in range(i + 1, len(allCols)):
                if isCompatible(i, j):
                    canBeNext[i].append(j)
                    canBeNext[j].append(i)
        
        @cache
        def dp(n: int, last: int) -> int:
            if n == 0:
                return 1
            res = 0
            for i in canBeNext[last]:
                res += dp(n - 1, i)
                res %= mod
            return res
        
        return dp(n, -1)
                