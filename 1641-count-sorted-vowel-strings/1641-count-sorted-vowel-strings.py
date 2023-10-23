class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        @cache
        def dp(index: int, prev: int) -> int:
            if index == n:
                return 1
            res = 0
            for i in range(prev, 5):
                res += dp(index + 1, i)
            return res
            
        return dp(0, 0)