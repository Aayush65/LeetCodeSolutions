class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        
        def toChange(val: int) -> int:
            ops = 0
            for i in nums:
                ops += abs(i - val)
            return ops
            
        if len(nums) % 2:
            median = nums[len(nums) // 2]
            return toChange(median)
        else:
            median1 = nums[len(nums) // 2]
            median2 = nums[len(nums) // 2 - 1]
            median3 = (median1 + median2) // 2
            median4 = ceil((median1 + median2) / 2)
            return min(toChange(median1), toChange(median2), toChange(median3), toChange(median4))