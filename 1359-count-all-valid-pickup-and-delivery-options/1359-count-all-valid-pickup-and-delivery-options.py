class Solution:
    def countOrders(self, n: int) -> int:
        mod = int(1e9 + 7)
        
        memo = [[-1] * (n + 1) for _ in range(n + 1)]
        memo[0][0] = 1
        
        def dp(p: int, d: int):
            if p < 0 or d < 0:
                return 0
            if memo[p][d] != -1:
                return memo[p][d]
            res = p * dp(p - 1, d + 1) + d * dp(p, d - 1)
            res %= mod
            memo[p][d] = res
            return res
            
            
        return dp(n, 0)