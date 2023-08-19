class Solution:
    def canMakeSubsequence(self, s1: str, s2: str) -> bool:
        
        @cache
        def dp(i: int, j: int) -> bool:
            if j == len(s2):
                return True
            if i == len(s1):
                return False
            if s1[i] == s2[j]:
                return dp(i + 1, j + 1)
            if (ord(s1[i]) - ord('a') + 1) % 26 == ord(s2[j]) - ord('a'):
                return dp(i + 1, j + 1)
            return dp(i + 1, j)
        
        
        return dp(0, 0)