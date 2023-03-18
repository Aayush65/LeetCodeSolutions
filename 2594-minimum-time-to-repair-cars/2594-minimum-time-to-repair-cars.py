class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(val: int) -> bool:
            count = 0
            for i in ranks:
                count += int((val / i) ** 0.5)
            return count >= cars
            
        lo = min(ranks)
        hi = max(ranks) * (cars ** 2)
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo