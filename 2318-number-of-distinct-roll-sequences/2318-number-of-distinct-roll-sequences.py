class Solution:
    def distinctSequences(self, n: int) -> int:
        mod = int(1e9 + 7)

        @cache
        def dp(n: int, prev1: int, prev2: int) -> int:
            if n == 0:
                return 1
            res = 0
            for i in range(1, 7):
                if i == prev1 or i == prev2:
                    continue
                if gcd(i, prev1) != 1:
                    continue
                res += dp(n - 1, i, prev1)
                res %= mod
            return res
        
        return dp(n, 7, 7)