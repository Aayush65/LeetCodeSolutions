class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(maxEle: int) -> bool:
            ops = 0
            for i in nums:
                if i > maxEle:
                    ops += ceil(i / maxEle) - 1
            return ops <= maxOperations

        lo = 1
        hi = max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo