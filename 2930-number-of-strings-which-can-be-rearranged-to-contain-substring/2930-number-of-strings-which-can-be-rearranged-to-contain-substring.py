class Solution:
    def stringCount(self, n: int) -> int:
        mod = int(1e9 + 7)

        @cache
        def dp(n: int, mask: int) -> int:
            if n == 0:
                return mask == 15
            res = dp(n - 1, mask) * 23
            res += dp(n - 1, mask | 1) + dp(n - 1, mask | 2)
            if mask & 4:
                res += dp(n - 1, mask | 8)
            else:
                res += dp(n - 1, mask | 4)
            return res % mod
            
        return dp(n, 0)    