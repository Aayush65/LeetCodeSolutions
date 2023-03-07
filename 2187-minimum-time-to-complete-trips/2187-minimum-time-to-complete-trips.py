class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(val: int) -> bool:
            trips = 0
            for i in time:
                trips += val//i
            return trips >= totalTrips

        maxTime = max(time)
        lo = 0
        hi = maxTime * totalTrips
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return hi