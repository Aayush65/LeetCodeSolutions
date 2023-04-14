class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        n = len(s)

        def dp(i: int, j: int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i] == s[j]:
                res = 2 + dp(i + 1, j - 1)
            else:
                res = max(dp(i + 1, j), dp(i, j - 1))
            memo[(i, j)] = res
            return res            

        return dp(0, n - 1)