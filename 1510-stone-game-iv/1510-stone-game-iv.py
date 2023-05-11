class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @cache
        def dp(n: int) -> bool:
            if not n:
                return False
            for i in range(1, int(n ** 0.5) + 1):
                if not dp(n - i ** 2):
                    return True
            return False
        
        return dp(n)