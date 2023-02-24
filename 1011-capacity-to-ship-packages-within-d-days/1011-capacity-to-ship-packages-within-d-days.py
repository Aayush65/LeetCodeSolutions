class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calcDays(capacity: int) -> int:
            day = 0
            w = 0
            for i in weights:
                w += i
                if w > capacity:
                    w = i
                    day += 1
                elif w == capacity:
                    w = 0
                    day += 1
            return day + 1 if w else day
        
        lo, hi = max(weights), sum(weights) 
        while lo < hi:
            mid = (lo + hi) // 2
            if calcDays(mid) > days:
                lo = mid + 1
            else:
                hi = mid
        return lo