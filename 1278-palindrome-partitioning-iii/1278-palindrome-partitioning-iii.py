class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        
        n = len(s)           

        @cache
        def palindromeCost(i: int, j: int) -> int:
            cost = 0
            while i < j:
                if s[i] != s[j]:
                    cost += 1
                i += 1
                j -= 1
            return cost

        @cache
        def dp(index: int, k: int) -> int:
            if k == 1:
                return palindromeCost(index, n - 1)
            res = float("inf")
            for i in range(index, n - k + 1):
                res = min(res, palindromeCost(index, i) + dp(i + 1, k - 1))
            return res
        
        return dp(0, k)