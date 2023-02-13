class Solution:
    def monkeyMove(self, n: int) -> int:
        mod = 1000000007
        def powerOf2(exp: int) -> int:
            if exp == 0:
                return 1
            if exp == 1:
                return 2
            if exp % 2:
                ans = powerOf2(exp // 2) % mod
                return (2 * ans * ans) % mod
            else:
                ans = powerOf2(exp // 2) % mod
                return (ans * ans) % mod
        return (powerOf2(n) - 2) %  mod