class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = int(1e9 + 7)
        
        @cache
        def dp(score: int, prev: int) -> int:
            if score < 0:
                return 0
            if score == 0:
                return 1
            res = 0
            val = (prev + 1) ** x
            if score - val >= 0:
                res += dp(score, prev + 1)
                res += dp(score - val, prev + 1)
                res %= mod
            return res
            
        return dp(n, 0)