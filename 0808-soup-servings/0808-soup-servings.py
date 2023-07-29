class Solution:
    def soupServings(self, n: int) -> float:
        servings = [(100, 0), (75, 25), (50, 50), (25, 75)]
        
        @cache
        def dp(n1: int, n2: int) -> list[int]:
            if n1 <= 0 and n2 <= 0:
                return 0.5
            if n1 <= 0:
                return 1
            if n2 <= 0:
                return 0
            
            res = 0
            for a, b in servings:
                res += dp(n1 - a, n2 - b)
            res /= 4
            return res

        return dp(n, n) if n < 5000 else 1