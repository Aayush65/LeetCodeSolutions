class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days.sort()
        
        @cache
        def dp(index: int) -> int:
            if index == len(days):
                return 0
            res = costs[0] + dp(index + 1)
            for i in range(index + 1, index + 8):
                if i == len(days):
                    res = min(res, costs[1])
                    break
                if days[i] > days[index] + 6:
                    res = min(res, costs[1] + dp(i))
                    break
            for i in range(index + 1, index + 31):
                if i == len(days):
                    res = min(res, costs[2])
                    break
                if days[i] > days[index] + 29:
                    res = min(res, costs[2] + dp(i))
                    break
            return res
        
        return dp(0) 