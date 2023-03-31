class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m = len(pizza)
        n = len(pizza[0])
        mod = 1000000007
        memo = {}

        def cut(row: int, col: int, persons: int) -> int:
            if (row, col, persons) in memo:
                return memo[(row, col, persons)]
            if row == m or col == n:
                return 0
            if not persons:
                for i in range(row, m):
                    for j in range(col, n):
                        if pizza[i][j] == 'A':
                            return 1
                return 0
            res = 0
            isFoundInRows = False
            for i in range(row, m):
                for j in range(col, n):
                    if pizza[i][j] == 'A':
                        isFoundInRows = True
                if isFoundInRows:
                    res += cut(i + 1, col, persons - 1)
            isFoundInCols = False
            for j in range(col, n):
                for i in range(row, m):
                    if pizza[i][j] == 'A':
                        isFoundInCols = True
                if isFoundInCols:
                    res += cut(row, j + 1, persons - 1)

            res %= mod
            memo[(row, col, persons)] = res
            return res
        
        return cut(0, 0, k - 1)