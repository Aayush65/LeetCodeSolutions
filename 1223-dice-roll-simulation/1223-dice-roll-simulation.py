class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = int(1e9 + 7)

        @cache
        def dp(n: int, last: int) -> int:
            if n == 0:
                return 1
            res = 0
            for i in range(6):
                if i == last:
                    continue
                for j in range(1, rollMax[i] + 1):
                    if j > n:
                        break
                    res += dp(n - j, i)
                    res %= mod
            return res
        
        return dp(n, -1)