class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = len(word1)
        w2 = len(word2)
        
        memo = {}
        def dp(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if i == w1:
                return w2 - j
            if j == w2:
                return w1 - i
            res = 0
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)
            res = 1 + min(dp(i, j + 1), dp(i + 1, j), dp(i + 1, j + 1))
            memo[(i, j)] = res
            return res
        
        return dp(0, 0)