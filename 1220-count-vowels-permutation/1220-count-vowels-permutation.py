class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = int(1e9 + 7)
        pattern = {-1: [0, 1, 2, 3, 4], 0: [1], 1: [0, 2], 2: [0, 1, 3, 4], 3: [2, 4], 4: [0]}
        
        @cache
        def dp(n: int, last: int) -> int:
            if n == 0:
                return 1
            res = 0
            for i in pattern[last]:
                res += dp(n - 1, i)
                res %= mod
            return res
        
        return dp(n, -1)
                