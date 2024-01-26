class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = int(1e9 + 7)
        
        @cache
        def dp(x: int, y: int, k: int) -> int:
            if not k or x in [-1, m] or y in [-1, n]:
                return 0
            res = 0
            if x == 0: res += 1
            if x == m - 1: res += 1
            if y == 0: res += 1
            if y == n - 1: res += 1
                
            res += dp(x + 1, y, k - 1) + dp(x - 1, y, k - 1) + dp(x, y + 1, k - 1) + dp(x, y - 1, k - 1)
            res %= mod
            return res
        
        return dp(startRow, startColumn, maxMove)