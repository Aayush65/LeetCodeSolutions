class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
    
        def coinsNeeded(coin: int, index: int, ans) -> int:
            if (coin, index) in memo:
                return memo[(coin, index)]
            if coin > amount or index == len(coins):
                return 0
            if coin == amount:
                # print(ans)
                return 1
            res = coinsNeeded(coin + coins[index], index, ans + [coins[index]]) + coinsNeeded(coin, index + 1, ans)
            memo[(coin, index)] = res
            return res
        
        ans = coinsNeeded(0,0,[])
        return ans