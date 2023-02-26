class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1 = len(s1)
        l2 = len(s2)
        
        memo = {}
        def dp(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if i == l1 and j == l2:
                return 0
            if i == l1:
                return ord(s2[j]) + dp(i, j + 1)
            elif j == l2:
                return ord(s1[i]) + dp(i + 1, j)
            if s1[i] == s2[j]:
                return dp(i + 1, j + 1)
            res = min(ord(s1[i]) + dp(i + 1, j), ord(s2[j]) + dp(i, j + 1))
            memo[(i, j)] = res
            return res
        
        return dp(0, 0)