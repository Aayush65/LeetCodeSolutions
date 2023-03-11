class Solution:
    def minCut(self, s: str) -> int:
        isPalindrome = lambda x: x == x[::-1]

        @cache
        def dfs(index: int) -> int:
            if index == len(s):
                return -1
            res = float("inf")
            for i in range(index + 1, len(s) + 1):
                if isPalindrome(s[index: i]):
                    res = min(res, 1 + dfs(i))
            return res

        return dfs(0)
        