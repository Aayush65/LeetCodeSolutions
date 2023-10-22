class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        
        isPalindrome = lambda x: x == x[::-1]
        
        @cache
        def dp(index: int, k: int) -> bool:
            if k == 1:
                return isPalindrome(s[index: n])
            for i in range(index + 1, n - k + 2):
                if isPalindrome(s[index: i]) and dp(i, k - 1):
                    return True
            return False
            
        return dp(0, 3)