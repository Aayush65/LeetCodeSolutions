class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums)):
            lo = max(i + 1, bisect_left(nums, lower - nums[i]))
            hi = bisect_left(nums, upper - nums[i] + 1)
            if hi - lo > 0:
                count += hi - lo
        return count
