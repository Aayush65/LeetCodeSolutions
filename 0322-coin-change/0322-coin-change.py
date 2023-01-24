class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def coinsNeeded(coin: int) -> int:
            if coin in memo:
                return memo[coin]
            if coin > amount:
                return float("inf")
            if coin == amount:
                return 0
            res = float("inf")
            for i in coins:
                res = min(1 + coinsNeeded(coin + i), res)
            memo[coin] = res
            return res
        
        ans = coinsNeeded(0)
        return ans if ans != float("inf") else -1