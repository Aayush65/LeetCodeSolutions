class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
    
        @cache
        def dp(l: int, r: int) -> int:
            if l == r:
                return 0
            if r - l == 1:
                return 1
            res = 100
            toRemove = 1 if s[l] == s[r - 1] else 0
            for i in range(l + 1, r):
                res = min(res, dp(l, i) + dp(i, r) - toRemove)
            return res

        return dp(0, n)