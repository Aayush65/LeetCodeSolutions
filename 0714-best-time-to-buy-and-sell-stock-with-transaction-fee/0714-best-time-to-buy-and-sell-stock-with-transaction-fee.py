class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        @cache
        def dp(index: int, toSell: False) -> int:
            if index == len(prices):
                return 0
            res = 0
            if toSell:
                res = prices[index] - fee + dp(index + 1, False)
            else:
                res = dp(index + 1, True) - prices[index]
            res = max(res, dp(index + 1, toSell))
            return res

        return dp(0, False)