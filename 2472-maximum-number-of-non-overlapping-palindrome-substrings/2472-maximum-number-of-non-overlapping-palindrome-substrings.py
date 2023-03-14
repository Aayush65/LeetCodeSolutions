class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        def isPalindrome(i: int, j: int) -> int:
            if i < 0:
                return False
            substr = s[i: j + 1]
            return substr == substr[::-1]
        
        dp = [0] * n
        for i in range(k - 1, n):
            if i > 0:
                dp[i] = dp[i - 1]
            
            if isPalindrome(i - k + 1, i):
                dp[i] = max(dp[i], 1 + dp[i - k])
            if isPalindrome(i - k, i):
                dp[i] = max(dp[i], 1 + dp[i - k - 1])
        return dp[-1]