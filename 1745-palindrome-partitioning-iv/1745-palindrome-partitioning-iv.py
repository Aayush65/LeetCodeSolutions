class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        
        @cache
        def dp(index: int, k: int) -> bool:
            if k == 1:
                return s[index: n] == s[index: n][::-1]
            for i in range(index + 1, n - k + 2):
                if s[index: i] == s[index: i][::-1] and dp(i, k - 1):
                    return True
            return False
            
        return dp(0, 3)