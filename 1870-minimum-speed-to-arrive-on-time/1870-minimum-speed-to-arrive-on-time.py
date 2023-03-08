class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def check(speed: int) -> bool:
            h = 0
            for i in dist:
                h = ceil(h)
                h += i / speed
            return h <= hour

        if len(dist) - 1 >= hour:
            return -1
        fraction = hour - int(hour)
        lo = 1
        hi = ceil(max(dist) / (hour - int(hour))) if fraction else max(dist)
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo