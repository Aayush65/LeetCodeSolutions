class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def check(maxVal: int) -> bool:
            count = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= maxVal:
                    count += 1
                    i += 1
                i += 1 
            return count >= p

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo