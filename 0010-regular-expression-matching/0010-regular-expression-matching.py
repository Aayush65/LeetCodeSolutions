class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(p)
        n = len(s)

        @cache
        def match(i: int, j: int) -> bool:
            if i == m and j == n:
                return True
            if i == m:
                return False
            res = False
            if i + 1 < m and p[i + 1] == '*':
                res = match(i + 2, j)
                for k in range(j, n):
                    if res or (s[k] != p[i] and p[i] != '.'):
                        break
                    if match(i + 2, k + 1):
                        res = True
            elif j < n and (p[i] == '.' or p[i] == s[j]):
                res = match(i + 1, j + 1)
            return res
        
        return match(0, 0)