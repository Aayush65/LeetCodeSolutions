class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = int(1e9 + 7)
        
        @cache
        def dp(index: int, prev: str) -> int:
            if index == len(s):
                return 1 if prev else 0
            res = dp(index + 1, s[index])
            if prev != s[index]:
                res += dp(index + 1, prev)
            res %= mod
            return res
        
        return dp(0, '')