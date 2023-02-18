class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return 0
        nums.sort()
        bb = nums[-3] - nums[0]
        bs = nums[-2] - nums[1]
        ss = nums[-1] - nums[2]
        return min(bb, bs, ss)