class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        
        @cache
        def dp(day: int, k: int) -> int:
            if k == 0:
                return 0
            index = bisect_left(events, day, key = lambda x: x[0])
            if index == len(events):
                return 0
            res = 0
            newIdx = bisect_left(events, day + 1, key = lambda x: x[0])
            if newIdx < len(events):
                res = dp(events[newIdx][0], k)
            for i in range(index, len(events)):
                if events[i][0] != events[index][0]:
                    break
                res = max(res, events[i][2] + dp(events[i][1] + 1, k - 1))
            return res
            
        
        return dp(1, k)