class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo = prices[0]
        maxProfit = 0
        for i in prices:
            lo = min(lo, i)
            maxProfit = max(maxProfit, i - lo)
        return maxProfit