class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def check(radius: int) -> int:
            h = 0
            for i in houses:
                while h < len(heaters) and i - heaters[h] > radius:
                    h += 1
                if h == len(heaters) or abs(heaters[h] - i) > radius:
                    return False
            return True
        
        houses.sort()
        heaters.sort()
        lo = 0
        hi = max(max(heaters) - min(houses), max(houses) - min(heaters))
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo