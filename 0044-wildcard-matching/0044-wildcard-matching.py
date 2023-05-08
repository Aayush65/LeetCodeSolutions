class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(p)
        n = len(s)
        
        memo = {}
        def match(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
            if i == m and j == n:
                return True
            if i == m or j > n:
                return False
            res = False
            if p[i] == '*':
                res = match(i + 1, j) or match(i, j + 1) or match(i + 1, j + 1)
            elif j < n and (p[i] == '?' or s[j] == p[i]):
                res = match(i + 1, j + 1)
            memo[(i, j)] = res
            return res
        
        return match(0, 0)