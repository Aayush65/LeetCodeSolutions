class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        
        @cache
        def dp(index: int, k: int) -> int:
            if index == n and k == 0:
                return 0
            if index == n or k == 0:
                return float("inf")
            res = float("inf")
            currDiff = 0
            for i in range(index, n):
                currDiff = max(currDiff, jobDifficulty[i])
                res = min(res, currDiff + dp(i + 1, k - 1))
            return res
        
        res = dp(0, d)
        return -1 if res == float("inf") else res
            