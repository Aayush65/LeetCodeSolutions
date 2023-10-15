class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = int(1e9 + 7)
        
        @cache
        def dp(pos: int, k: int) -> int:
            if k == 0:
                return 1 if pos == 0 else 0
            res = dp(pos, k - 1) % mod
            if pos > 0:
                res += dp(pos - 1, k - 1)
                res %= mod
            if pos < arrLen - 1:
                res += dp(pos + 1, k - 1)
                res %= mod
            return res   
        
        return dp(0, steps)