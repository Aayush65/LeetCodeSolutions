class Solution:
    def minSteps(self, num: int) -> int:
        
        @cache
        def dp(n: int, copy: int) -> int:
            if n == num:
                return 0
            if n > num:
                return float("inf")
            return min(2 + dp(n * 2, n), 1 + dp(n + copy, copy))
        
        return 2 + dp(2, 1) if num > 1 else 0