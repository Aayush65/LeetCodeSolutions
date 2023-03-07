class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(val: int) -> bool:
            if not val:
                return False
            hours = 0
            for i in piles:
                hours += ceil(i / val)
            return hours <= h

        hi = max(piles)
        lo = 0
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
