class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        schedule = sorted([[startTime[i], endTime[i], profit[i]] for i in range(n)])
        startTime = [i[0] for i in schedule]
        endTime = [i[1] for i in schedule]
        profit = [i[2] for i in schedule]
    
        memo = {}
        def dp(index: int) -> int:
            if index >= n:
                return 0
            if index in memo:
                return memo[index]
            nextSlot = bisect_left(startTime, endTime[index])
            maxProfit = profit[index]
            for i in range(nextSlot, n):
                if startTime[i] >= endTime[index]: 
                    maxProfit += dp(i)
                    break
            maxProfit = max(maxProfit, dp(index + 1))
            memo[index] = maxProfit
            return maxProfit

        return dp(0)