class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        for pile in piles:
            for i in range(1, len(pile)):
                pile[i] += pile[i - 1]

        @cache
        def dp(index: int, k: int) -> int:
            if not k or index == len(piles):
                return 0
            res = dp(index + 1, k)
            for i in range(len(piles[index])):
                if k < i + 1:
                    break
                res = max(res, piles[index][i] + dp(index + 1, k - i - 1))
            return res
        
        return dp(0, k)