class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        crimes = [(noOfCriminals, profits) for noOfCriminals, profits in zip(group, profit)]
        crimes.sort(key = lambda x: [x[0], -x[1]])
        mod = 1000000007
        
        @cache
        def dp(index: int, n: int, score: int) -> int:
            if index == len(crimes) or n < crimes[index][0]:
                return 1 if score >= minProfit else 0
            res = dp(index + 1, n, score)
            # if n >= crimes[index][0]:
            res += dp(index + 1, n - crimes[index][0], min(score + crimes[index][1], minProfit))
            return res % mod
            
        return dp(0, n, 0)