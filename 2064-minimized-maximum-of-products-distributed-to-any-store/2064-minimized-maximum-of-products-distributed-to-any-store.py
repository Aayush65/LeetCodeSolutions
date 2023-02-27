class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(items: int) -> bool:
            shops = 0
            for i in quantities:
                shops += i // items
                if i % items:
                    shops += 1
                if shops > n:
                    return False
            return True
        
        hi = max(quantities)
        lo = 1
        while lo < hi:
            mid = (lo + hi) // 2
            if not check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo