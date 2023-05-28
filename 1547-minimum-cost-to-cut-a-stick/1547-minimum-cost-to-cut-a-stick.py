class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
    
        @cache
        def dp(l: int, r: int) -> int:
            startIdx = bisect_right(cuts, l)
            endIdx = bisect_left(cuts, r)
            if startIdx == endIdx:
                return 0
            cost = float("inf")
            for i in range(startIdx, endIdx):
                cost = min(cost, dp(l, cuts[i]) + dp(cuts[i], r))
            cost += r - l
            return cost

        return dp(0, n)