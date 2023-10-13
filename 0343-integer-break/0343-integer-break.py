class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def dp(n: int):
            if memo[n] != -1:
                return memo[n]
            if not n:
                return 1
            res = 1
            for i in range(2, n + 1):
                res = max(res, i * dp(n - i))
            memo[n] = res
            return res

        if n < 4:
            return {2: 1, 3: 2}[n]
        return dp(n)