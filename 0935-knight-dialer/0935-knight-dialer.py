class Solution:
    def knightDialer(self, n: int) -> int:
        mod = int(1e9 + 7)
        paths = {-1: [i for i in range(10)], 0: [4,6], 1: [6,8], 2: [7,9], 3: [4,8], 4: [0,3,9], 5: [], 6: [0,1,7], 7: [2,6], 8: [1,3], 9:[2,4]}
        
        @cache
        def dp(n: int, k: int) -> int:
            if k == 0:
                return 1
            res = 0
            for i in paths[n]:
                res += dp(i, k - 1)
                res %= mod
            return res
        
        return dp(-1, n)